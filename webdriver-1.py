from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the python.org website
    driver.get("https://www.python.org")

    # Find the introduction element by its class name
    intro_element = driver.find_element(By.CLASS_NAME, "introduction")
    print(intro_element.text)

    # Find the news section and extract headlines
    news_items = driver.find_elements(By.CSS_SELECTOR, ".list-recent-posts li")

    print("Latest News from Python.org:")
    for item in news_items:
        title = item.find_element(By.TAG_NAME, "a").text
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(f"- {title}: {link}")

finally:
    # Close the browser
    driver.quit() 
