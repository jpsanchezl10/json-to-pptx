from src.presentation import create_presentation
import json


def main():
    # Read the JSON data
    with open('./src/json/presentation.json', 'r') as file:
        slides_data = json.load(file)

    # Create the presentation
    create_presentation(slides_data)

if __name__ == '__main__':
    main()