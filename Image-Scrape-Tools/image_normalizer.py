import sys
import os

# make sure you're logged in with `huggingface-cli login`
from huggingface_hub import login

login()

import distutils
try:
    import distutils.core
    print("distutils is available")
except ModuleNotFoundError:
    print("distutils is not available")

try:
    import setuptools
    print("setuptools is available")
except ModuleNotFoundError:
    print("setuptools is not available")

import csv
import os
import requests
from io import BytesIO
from PIL import Image as PILImage, UnidentifiedImageError
from googleapiclient.discovery import build
import numpy as np
import re
import pandas as pd

def fetch_image_url(service, query):
    try:
        result = service.cse().list(q=query, cx=GOOGLE_CSE_ID, searchType="image", num=1).execute()
        items = result.get("items", [])
        if items:
            return items[0]["link"]
        else:
            print(f"No image found for query: {query}")
            return None
    except Exception as e:
        print(f"Error fetching image URL: {e}")
        return None

def resize_and_normalize_image(file_path, target_size=(512, 512)):
    try:
        img = PILImage.open(file_path)
        img = img.resize(target_size, PILImage.LANCZOS)
        img_array = np.array(img) / 255.0
        resized_normalized_path = os.path.splitext(file_path)[0] + "_resized_normalized.jpg"
        img_resized_normalized = PILImage.fromarray((img_array * 255).astype(np.uint8))
        img_resized_normalized.save(resized_normalized_path)
        return resized_normalized_path
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def download_image(image_url, index):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            img = PILImage.open(BytesIO(response.content))
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            image_name = f"downloaded_img_png(test1){index}.png"  # Change the file extension to .png
            img.save(image_name, format="PNG")  # Save the image as PNG format
            return image_name
        else:
            print(f"Error: Failed to download image from {image_url}")
    except (UnidentifiedImageError, Exception) as e:
        print(f"Error: {e}")
    return None

# Initialize the Google Custom Search service with your API key
GOOGLE_API_KEY = ''
GOOGLE_CSE_ID = ''
# GOOGLE_CSE_ID = ''
service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

csv_file_path = 'CSE144/prompts.csv'
output_csv_file_path = 'dataset(test1).csv'

def extract_text_from_prompt(prompt):
    match = re.search(r'([^\d]+)', prompt)
    if match:
        return match.group(1).strip()
    else:
        return prompt

# Create an empty list to store rows with valid images
valid_rows = []

with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for i, row in enumerate(csvreader, start=1):
        prompt = ','.join(row)
        print(f"Processing prompt: {prompt}")
        text = extract_text_from_prompt(prompt)

        try:
            image_url = fetch_image_url(service, text)
            if image_url:
                print(f"Image URL found: {image_url}")
                image_name = download_image(image_url, i)
                if image_name:
                    print("Image downloaded successfully")
                    valid_rows.append([text, image_name])
                else:
                    print("Error: Image could not be downloaded")
            else:
                print("Error: Image URL not found")
        except Exception as e:
            print(f"Error processing prompt: {e}")

# Create a DataFrame from the list of valid rows
df = pd.DataFrame(valid_rows, columns=['text', 'image'])

# Save the DataFrame to CSV
df.to_csv(output_csv_file_path, index=False)

print(f"CSV file with prompts and image names saved to: {output_csv_file_path}")
