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

# Loop through each details element
for details_element in details_elements:
    # Find the anchor tag within the details element
    anchor = details_element.find('a')
    
    # Get the href attribute of the anchor
    anchor_href = anchor['href'] if anchor and 'href' in anchor.attrs else ''
    
    # Get the text inside the anchor
    anchor_text = anchor.get_text(strip=True) if anchor else ''

    # Find the paragraph tag within the details element
    paragraph = details_element.find('p')
    
    # Get the text inside the paragraph
    description = paragraph.get_text(strip=True) if paragraph else ''
    
    # Append the extracted data to the list
    data.append({'Website link': anchor_href, 'Title': anchor_text, 'Description': description})

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = "scraped_data2.csv"
df.to_csv(csv_filename, index=False)

print("Data has been scraped and saved to", csv_filename)
