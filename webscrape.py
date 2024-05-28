import requests
import os
from PIL import Image

def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return True
    return False

def check_disk_space(threshold=100):
    """Check if the available disk space is above a certain threshold (in MB)."""
    st = os.statvfs('/')
    free_space = st.f_bavail * st.f_frsize / (1024 * 1024)  # Convert to MB
    return free_space > threshold

def compress_image(file_path, quality=85):
    """Compress the image to reduce its size."""
    try:
        img = Image.open(file_path)
        img.save(file_path, optimize=True, quality=quality)
        return True
    except Exception as e:
        print(f"Error compressing image: {e}")
        return False

def main():
    # Replace with your actual Google Custom Search API key and CX
    api_key = 'AIzaSyBI-nqVD-7pvcc1onML5znYdAXTUOiE_Fg'
    cx = '47f4302be37f24705'

    query = input("Enter your prompt: ")

    if not check_disk_space():
        print("Not enough disk space available.")
        return

    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cx}&key={api_key}&searchType=image"
    response = requests.get(search_url)
    results = response.json()

    if 'items' in results:
        # Taking the first image result
        first_image_url = results['items'][0]['link']
        print(f"Image URL: {first_image_url}")

        image_path = 'downloaded_image.jpg'
        if download_image(first_image_url, image_path):
            print(f"Image successfully downloaded and saved as {image_path}.")
            if compress_image(image_path):
                print(f"Image compressed and saved as {image_path}.")
            else:
                print("Failed to compress image.")
        else:
            print("Failed to download image.")
    else:
        print("No images found for the prompt.")

if __name__ == "__main__":
    main()
