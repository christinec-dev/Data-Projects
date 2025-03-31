# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

#region EXTRACTION
def get_soup_from_driver(driver):
    """Get a BeautifulSoup object from a Selenium WebDriver"""
    return bs(driver.page_source, 'html.parser')

def get_job_details(driver):
    """Extract job details"""
    jobs = []
    base_url = "https://www.google.com/about/careers/applications/jobs/results/"
    # Navigate through pages 1 to 3
    for page in range(1, 4):
        # Parse the loaded page
        url = f"{base_url}?page={page}"
        driver.get(url)
        time.sleep(2)  
        soup = get_soup_from_driver(driver)

        # Find all job elements
        link_elements = soup.find_all('a', class_='WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb')
        title_elements = soup.find_all('h3', class_='QJPWVe')
        company_elements_outer = soup.find_all('span', class_='RP7SMd')
        company_elements_inner = [outer_span.find('span') for outer_span in company_elements_outer]
        location_elements = soup.find_all('span', class_='r0wTof')
        level_elements = soup.find_all('span', class_='wVSTAb')
        min_length = min(len(title_elements), len(link_elements), len(company_elements_inner), len(location_elements), len(level_elements))

        # Extract text or attributes from each element
        for i in range(min_length):
            link = 'https://www.google.com/about/careers/applications/' + link_elements[i]['href']
            title = title_elements[i].text.strip()
            company = company_elements_inner[i].text.strip()
            location = location_elements[i].text.strip()
            level = level_elements[i].text.strip()

            # Navigate to the job detail page to extract the description
            driver.get(link) 
            time.sleep(2) 
            job_soup = get_soup_from_driver(driver)
            
            # Replace with actual class for description
            description_element = job_soup.find('div', class_='KwJkGe')  
            description = description_element.text.strip() if description_element else "No description available"
            jobs.append((title, link, company, location, description, level))
    return jobs

# Set up Selenium WebDriver (in this case Chrome)
driver = webdriver.Chrome() 

# Get job details
job_details = get_job_details(driver)

# Convert to DataFrame
df = pd.DataFrame(job_details, columns=['Title', 'Link', 'Company', 'Location', 'Description', 'Level'])

# Close the driver
driver.quit()

#endregion

#region PREPROCESSING

# Replace odd values with appropriate strings
df_copy = df.copy()
df_copy['Description'] = df_copy['Description'].str.replace("info_outlineX", "")
df_copy['Description'] = df_copy['Description'].str.replace("Info ", "")
df_copy['Description'] = df_copy['Description'].str.replace("\n", " ")
df_copy['Location'] = df_copy['Location'].str.replace(";", "")

#endregion

#region EXPORTING

# File names
csv_file = 'google_jobs_data.csv'
excel_file = 'google_jobs_data.xlsx'

# Export to CSV
try:
    df_copy.to_csv(csv_file, index=False)
    print(f"Data exported to {csv_file}")
except PermissionError as e:
    print(f"Permission error while writing to {csv_file}: {e}")

# Export to Excel
try:
    df_copy.to_excel(excel_file, index=False, sheet_name='Google Jobs Data')
    print(f"Data exported to {excel_file}")
except PermissionError as e:
    print(f"Permission error while writing to {excel_file}: {e}")

#endregion