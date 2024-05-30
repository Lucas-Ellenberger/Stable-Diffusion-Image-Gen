import csv
import requests
from io import BytesIO
from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Path to the specific version of ChromeDriver compatible with your Chrome browser
chromedriver_path = "/Users/niranjanabalaji/cse/cse144/dallemini/chromedriver"

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run headless Chrome
service = ChromeService(executable_path=chromedriver_path, port=0)
print("no help")
driver = webdriver.Chrome(service=service, options=options)
print("help")

def fetch_image_url(driver, query):
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    driver.get(search_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    image_tag = soup.find('img', {'class': 't0fcAb'})  # Find the first image
    return image_tag['src'] if image_tag else None

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    return None

# Define the path to the CSV file
csv_file_path = 'test-prompts.csv'

# Create a new Excel workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active

# Set the headers
worksheet.append(['Prompt', 'Image'])

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # Skip the header

    # Process each row in the CSV file
    for i, row in enumerate(csvreader):
        prompt = row[0]
        image_url = fetch_image_url(driver,prompt)
        
        if image_url:
            image = download_image(image_url)
            if image:
                # Save the image to a temporary file
                image_file_path = f'image_{i}.png'
                image.save(image_file_path)

                # Create an Excel image object
                excel_image = ExcelImage(image_file_path)

                # Append the prompt to the worksheet
                worksheet.append([prompt, ''])

                # Add the image to the worksheet in the appropriate cell
                image_cell = f'B{i+2}'  # Adjust for header row
                worksheet.add_image(excel_image, image_cell)
            else:
                worksheet.append([prompt, 'Image not found'])
        else:
            worksheet.append([prompt, 'Image not found'])

# Save the workbook to a file
excel_file_path = 'dataset_with_images.xlsx'
workbook.save(excel_file_path)
print(f'Saved Excel file with images to {excel_file_path}')

# Close the Selenium WebDriver
driver.quit()
