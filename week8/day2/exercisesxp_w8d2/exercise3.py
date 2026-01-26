# Exercise 3 : Scrape Dynamic Content from Rotten Tomatoes

# Use Selenium to navigate to the Rotten Tomatoes Certified Fresh Movies page.
# Extract the HTML content after it’s fully loaded.
# Use BeautifulSoup to parse and extract the movie titles, scores, and release dates.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up
from bs4 import BeautifulSoup
import requests

options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options) 
url = "https://editorial.rottentomatoes.com/guide/best-christmas-movies/"
driver.get(url)
wait = WebDriverWait(driver, 10)


# Extract the HTML content using driver.page_source.
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup.
soup = BeautifulSoup(html_content, 'html.parser')

# Find and extract the desired movie information.
target = "elf"

for movie in soup.select("div.countdown-item-content"):
    title = movie.find("a").text.strip().lower()
    score = movie.find("span", class_="tMeterScore").text.strip()
    year = movie.find("span", class_="start-year").text.strip()

    if target in title:
        print({
            "title": title.title(),
            "score": score,
            "year": year,    
        })
        break

