import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'http://example.com'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract text from the webpage
text = soup.get_text()

# Print the extracted text
print(text)
