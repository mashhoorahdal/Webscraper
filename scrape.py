import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page you want to scrape
url = "https://trustanalytica.com/us/best-spa"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all elements with class "sr-item-details"
details_elements = soup.find_all('div', class_='sr-item-details')

# Create lists to store the extracted data
data = []

# Find all div elements with class "sr-item"
div_elements = soup.find_all('div', class_='sr-item')

# Loop through each div element
for div_element, details_element in zip(div_elements, details_elements):
    # Find all images within the div and print their src
    images = div_element.find_all('img')
    for image in images:
        image_src = image.get('src', '')

        # Find the anchor tag within the details element
        anchor = details_element.find('a')

        # Get the href attribute of the anchor
        anchor_href = anchor['href'] if anchor and 'href' in anchor.attrs else ''

        # Get the text inside the anchor
        anchor_text = anchor.get_text(strip=True) if anchor else ''

        # Find the paragraph tag within the details element
        paragraph = details_element.find('p')

        # Get the text inside the paragraph
        paragraph_text = paragraph.get_text(strip=True) if paragraph else ''
        
        # Find the address within the div element
        address_span = div_element.find('div', class_='sr-ci-text').find('span')
        address = address_span.get_text(strip=True) if address_span else ''
        
        # Find the contact information within the div element
        phone_div = div_element.find('div', class_='sr-ci-text').find('strong')
        phone_number = phone_div.get_text(strip=True) if phone_div else ''

        # Append the extracted data to the list
        data.append({'Anchor Href': anchor_href, 'Anchor Text': anchor_text, 'Paragraph Text': paragraph_text, 'Image Src': image_src, 'Address': address, 'Phone Number': phone_number})

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = "scraped_data.csv"
df.to_csv(csv_filename, index=False)

print("Data has been scraped and saved to", csv_filename)
