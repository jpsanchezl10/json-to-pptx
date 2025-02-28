import json
import requests
from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Unsplash API access key - replace with your own
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def download_image(query):
    search_url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": 1,
        "client_id": UNSPLASH_ACCESS_KEY
    }

    try:
        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["results"]:
            img_url = data["results"][0]["urls"]["regular"]
            img_response = requests.get(img_url, timeout=5)
            img_response.raise_for_status()
            img_data = img_response.content

            img_path = f"images/{query.replace(' ', '_')}.jpg"
            with open(img_path, 'wb') as handler:
                handler.write(img_data)
            logger.info(f"Successfully downloaded image for query: {query}")
            return img_path
        else:
            logger.warning(f"No images found for query: {query}")
    except Exception as e:
        logger.error(f"Error during image search for query {query}: {str(e)}")

    return None

def create_presentation(slides_data):
    prs = Presentation()
    layout = prs.slide_layouts[5]  # Blank slide layout

    if not os.path.exists('images'):
        os.makedirs('./images')

    for slide_data in slides_data:
        slide = prs.slides.add_slide(layout)
        
        # Set the slide title
        title_shape = slide.shapes.title
        title_shape.text = slide_data['title']

        # Add the speech text as a text box
        left = Inches(1)
        top = Inches(5)
        width = Inches(8)
        height = Inches(1.5)
        tx_box = slide.shapes.add_textbox(left, top, width, height)
        tf = tx_box.text_frame
        p = tf.add_paragraph()
        # p.text = slide_data['speech']
        p.font.size = Pt(14)
        p.font.color.rgb = RGBColor(0, 0, 0)

        # Download and add the image
        image_path = download_image(slide_data['image'])
        if image_path:
            img_left = Inches(1)
            img_top = Inches(2.5)
            img_width = Inches(8)
            img_height = Inches(4.5)
            slide.shapes.add_picture(image_path, img_left, img_top, img_width, img_height)
        else:
            logger.error(f"Failed to download image for query: {slide_data['image']}")

    prs.save("SanchezJuan_video_presentation_week3.pptx")
