import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = "https://trustanalytica.com/us/best-spa"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all div elements with class "sr-item"
div_elements = soup.find_all('div', class_='sr-item')

# Loop through each div element
for div_element in div_elements:
    # Find all images within the div and print their titles
    images = div_element.find_all('img')
    for image in images:
        if 'title' in image.attrs:
            image_title = image['title']
            print(image_title)
