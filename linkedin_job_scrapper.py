import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape job details
def scrape_job_details(job_id):
    job_url = f"https://www.linkedin.com/jobs/view/{job_id}"
    print(job_url)
    job_response = requests.get(job_url)

    if job_response.status_code != 200:
        print(f"Failed to retrieve job details for Job ID: {job_id}")
        return None

    job_soup = BeautifulSoup(job_response.text, "html.parser")

    job_post = {}

    try:
        job_post["job_title"] = job_soup.find("h1", {"class": "top-card-layout__title"}).text.strip()
    except:
        job_post["job_title"] = None

    try:
        job_post["company_name"] = job_soup.find("a", {"class": "topcard__org-name-link"}).text.strip()
    except:
        job_post["company_name"] = None

    try:
        job_post["job_url"] = job_url
    except:
        job_post["job_url"] = None

    try:
        job_post["job_description"] = job_soup.find("div", {"class": "show-more-less-html__markup"}).get_text(separator='\n').strip()
    except:
        job_post["job_description"] = None

    return job_post

# Get user input
title = input("Enter job title (e.g., Software Engineer): ").strip()
location = input("Enter location (e.g., United States): ").strip()
page_number = int(input("Enter page number (0 for the first page): ").strip())

# Set search parameters
list_url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={title}&location={location}&start={page_number}"
response = requests.get(list_url)

if response.status_code != 200:
    print(f"Failed to retrieve job listings from {list_url}")
    exit()

list_soup = BeautifulSoup(response.text, "html.parser")
page_jobs = list_soup.find_all("li")

job_list = []

# Iterate through job listings
for job in page_jobs:
    base_card_div = job.find("div", {"class": "base-card"})

    if base_card_div and base_card_div.get("data-entity-urn"):
        job_id = base_card_div.get("data-entity-urn").split(":")[3]

        job_details = scrape_job_details(job_id)
        if job_details:
            job_list.append(job_details)
    else:
        print("Job not found because element not found.")

# Create DataFrame and save to CSV
jobs_df = pd.DataFrame(job_list)
jobs_df.to_csv('jobs.csv', index=False)

print(f"Scraped {len(jobs_df)} job postings. Data saved to 'jobs.csv'.")
