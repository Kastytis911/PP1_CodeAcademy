
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url1 = 'https://www.audimas.lt/katalogas/vyrams/striukes/'
url2 = 'https://www.audimas.lt/katalogas/moterims/striukes/'


# Send an HTTP request to the webpage and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the listings on the page
#listings = soup.find_all('div', class_='auto-lists lt')
listings = soup.find_all('div', class_='product_element multiple-photos')



# Loop through the listings and extract the relevant information
for listing in listings:

    # Get the title and price of the listing
    title = listing.find('span', class_='title').text.strip()
    price = listing.find('span', class_='price discount').text.strip()

    # Print the information of the listing
    print(title)
    print(price)




