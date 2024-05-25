import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_job_details(job_url):
# Send a GET request to the job detail page
job_response = requests.get(job_url, headers={'User-Agent': 'Mozilla/5.0'})
job_soup = BeautifulSoup(job_response.text, 'html.parser')

# Extract job details - replace the following selectors with actual selectors from the job detail page
job_title = job_soup.select_one('job_title_selector').text.strip()
job_description = job_soup.select_one('job_description_selector').text.strip()
job_location = job_soup.select_one('job_location_selector').text.strip()
# Add more details as needed

return {
'Title': job_title,
'Description': job_description,
'Location': job_location
# Add more details as needed
}

def scrape_jobs(url):
# Send a GET request to the website
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find job listings - replace 'job_listing_selector' with the actual selector that contains each job link
job_listings = soup.select('job_listing_selector')

jobs_data = []
for job_elem in job_listings:
# Extract the URL of the job detail page
job_detail_url = job_elem.select_one('job_detail_link_selector')['href']
# Scrape job details from the job detail page
job_data = scrape_job_details(job_detail_url)
jobs_data.append(job_data)

return jobs_data

def main():
# Prompt the user for the URL
url = input("Please enter the URL of the Capgemini job listings page: ")

# Call the scrape_jobs function with the provided URL
jobs_data = scrape_jobs(url)

# Create a DataFrame and save to Excel
df = pd.DataFrame(jobs_data)
excel_filename = 'capgemini_job_listings.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data has been saved to {excel_filename}")

if __name__ == "__main__":
main()