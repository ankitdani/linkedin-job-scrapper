# LinkedIn Job Scraper

This repository contains a Python script that scrapes job listings from LinkedIn based on user-provided job title and location. The script retrieves job details, including the job title, company name, job description, and job URL, and saves them to a CSV file. The script is designed to be used without requiring the user to log in.

## Features

- Scrape job listings from LinkedIn based on specified job title and location.
- Retrieve detailed information for each job listing, including:
  - Job Title
  - Company Name
  - Job Description
  - Job URL
- Save the scraped data to a CSV file.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup4 library
- Pandas library

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/linkedin-job-scraper.git
    cd linkedin-job-scraper
    ```

2. Install the required Python packages:

    ```
    pip3 install requests beautifulsoup4 pandas
    ```

## Usage

1. Run the script:

    ```
    python3 linkedin_job_scraper.py
    ```

2. Enter the job title, location, and page number when prompted:

    ```
    Enter job title (e.g., Software Engineer): Software Engineer
    Enter location (e.g., United States): United States
    Enter page number (0 for the first page): 0
    ```

3. The script will scrape the job listings and save the data to `jobs.csv`.

## Notes

- The script retrieves job listings from LinkedIn using publicly accessible URLs. 
- The script might need adjustments if LinkedIn changes its website structure.
