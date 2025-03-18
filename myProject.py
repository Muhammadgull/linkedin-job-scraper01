import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# LinkedIn Login Credentials
LINKEDIN_USERNAME = "muhammadgul.ims@gmail.com"  # Change this
LINKEDIN_PASSWORD = "Mgbkbs@1122"           # Change this

# Job search details
JOB_TITLE = "IT Engineer"
JOB_LOCATION = "Saudi Arabia"
MAX_PAGES = 5  # Number of pages to scrape

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open LinkedIn Login Page
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Step 2: Enter Login Credentials
    driver.find_element(By.ID, "username").send_keys(LINKEDIN_USERNAME)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 3: Navigate to LinkedIn Jobs Page
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)

    # Step 4: Enter Job Title & Location
    search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search by title, skill, or company']")
    search_box.send_keys(JOB_TITLE)
    time.sleep(1)
    
    location_box = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
    location_box.clear()
    location_box.send_keys(JOB_LOCATION)
    time.sleep(1)
    
    location_box.send_keys(Keys.RETURN)
    time.sleep(5)

    job_list = []
    
    # Step 5: Extract jobs from multiple pages
    for page in range(1, MAX_PAGES + 1):
        print(f"🔄 Scraping page {page}...")
        time.sleep(3)
        
        # Find job listings
        jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
        
        for job in jobs:
            try:
                job_title = job.find_element(By.CSS_SELECTOR, "h3").text
                company_name = job.find_element(By.CSS_SELECTOR, "h4").text
                job_link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                job_list.append({
                    "Job Title": job_title,
                    "Company": company_name,
                    "Job Link": job_link
                })
            except:
                continue

        # Try to find "Next Page" button
        try:
            next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(2)
            next_button.click()
        except:
            print("⚠️ No more pages found.")
            break

    # Save to Excel
    df = pd.DataFrame(job_list)
    df.to_excel("linkedin_jobs.xlsx", index=False)
    print(f"✅ {len(job_list)} jobs saved to 'linkedin_jobs.xlsx'.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
    print("✅ Browser closed.")
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# LinkedIn Login Credentials
LINKEDIN_USERNAME = "muhammadgul.ims@gmail.com"  # Change this
LINKEDIN_PASSWORD = "Mgbkbs@1122"           # Change this

# Job search details
JOB_TITLE = "Software Tester"
JOB_LOCATION = "Saudi Arabia"
MAX_PAGES = 5  # Number of pages to scrape

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open LinkedIn Login Page
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Step 2: Enter Login Credentials
    driver.find_element(By.ID, "username").send_keys(LINKEDIN_USERNAME)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 3: Navigate to LinkedIn Jobs Page
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)

    # Step 4: Enter Job Title & Location
    search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search by title, skill, or company']")
    search_box.send_keys(JOB_TITLE)
    time.sleep(1)
    
    location_box = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
    location_box.clear()
    location_box.send_keys(JOB_LOCATION)
    time.sleep(1)
    
    location_box.send_keys(Keys.RETURN)
    time.sleep(5)

    job_list = []
    
    # Step 5: Extract jobs from multiple pages
    for page in range(1, MAX_PAGES + 1):
        print(f"🔄 Scraping page {page}...")
        time.sleep(3)
        
        # Find job listings
        jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
        
        for job in jobs:
            try:
                job_title = job.find_element(By.CSS_SELECTOR, "h3").text
                company_name = job.find_element(By.CSS_SELECTOR, "h4").text
                job_link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                job_list.append({
                    "Job Title": job_title,
                    "Company": company_name,
                    "Job Link": job_link
                })
            except:
                continue

        # Try to find "Next Page" button
        try:
            next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(2)
            next_button.click()
        except:
            print("⚠️ No more pages found.")
            break

    # Save to Excel
    df = pd.DataFrame(job_list)
    df.to_excel("linkedin_jobs.xlsx", index=False)
    print(f"✅ {len(job_list)} jobs saved to 'linkedin_jobs.xlsx'.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
    print("✅ Browser closed.")
