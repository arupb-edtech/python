from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver
driver = webdriver.Chrome()

try:
    # Open the Indeed website
    driver.get("https://www.indeed.com")

    # Find the search box for job titles/keywords
    search_box = driver.find_element(By.ID, "text-input-what")
    search_box.send_keys("Python Developer")

    # Find the search box for location
    location_box = driver.find_element(By.ID, "text-input-where")
    location_box.clear()
    location_box.send_keys("remote")

    # Submit the search form
    location_box.send_keys(Keys.RETURN)

    # Wait for page to load
    time.sleep(3)

    # Search job postings
    job_cards = driver.find_elements(By.CSS_SELECTOR, "job_seen_beacon")

    print("Job Listings:")
    for job in job_cards:
        try:
            # Extract job title
            title = job.find_element(By.CLASS_NAME, "jobTitle").text

            # Extract company name
            company = job.find_element(By.CLASS_NAME, "companyName").text

            # Extract location
            location = job.find_element(By.CLASS_NAME, "companyLocation").text

            print(f"- Title: {title}")
            print(f"- Company: {company}")
            print(f"- Location: {location}")
        except Exception as e:
            print("Error extracting jon details", e)
finally:
    # Close the browser

    driver.quit()

