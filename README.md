Juan Pablo Sanchez Lorenzo, 
Cybersecurity Researcher

# JSON to PowerPoint Presentation Generator

This tool automatically generates a PowerPoint presentation from a JSON file, fetching relevant images from Unsplash for each slide.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory in your terminal.

3. Install the required Python packages:

pip install -r requirements.txt

4. Sign up for a free Unsplash developer account at https://unsplash.com/developers and create a new application to get an access key.

5. Create a .env file in the project directory and add your Unsplash access key:

echo "UNSPLASH_ACCESS_KEY=your_actual_access_key_here" >> .env

Replace `your_actual_access_key_here` with your Unsplash access key.

## Usage

1. Prepare your presentation content in a JSON file named `presentation.json`. The JSON should have the following structure:

```json
[
  {
    "slide": 0,
    "title": "Slide Title",
    "speech": "Slide content or speaker notes",
    "image": "Image description for Unsplash search"
  },
  ...
]

Run the script:

python main.py


3. The script will generate a PowerPoint file named Presentation.pptx in the same directory.

JSON File Format
Each slide in the presentation.json file should contain the following fields:

slide: Slide number (starting from 0)
title: The title of the slide
speech: Content or speaker notes for the slide
image: A description of the image to be searched on Unsplash

Example:

{
  "slide": 0,
  "title": "Introduction to Our Topic",
  "speech": "Welcome everyone. Today, we'll be discussing...",
  "image": "abstract background with blue geometric shapes"
}

Troubleshooting

If you encounter any issues with image downloads, check your Unsplash API key in the .env file and ensure you haven't exceeded the rate limit (50 requests per hour for free accounts).
Make sure your presentation.json file is in the correct format and in the same directory as main.py.
Ensure that the .env file is in the project root directory and contains the correct API key.

Notes

The tool uses Unsplash for images. While these may not be as specific as custom-selected images, they should be high-quality and relevant to the topics.
Remember to comply with Unsplash's attribution requirements in your final presentation.
For more specific images, consider manually selecting and placing them in your presentation after it's generated.
Keep your .env file secure and do not share it publicly, as it contains your API key.

License
This project is open source and available under the Apache 2.0 License.
