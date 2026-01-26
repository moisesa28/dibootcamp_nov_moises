#xercise 5 : Scrape and Analyze Weather Data from a JavaScript-Enabled Weather Website

from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import time
import pprint

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"
driver.get(url)

# Give JavaScript time to load
time.sleep(5)

#Scroll to Ensure All Forecast Cards Load
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

#Parse Rendered HTML with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


# Locate Forecast Cards
# <div class="daily-list content-module">


daily_list = soup.select_one("div.daily-list.content-module")

if not daily_list:
    print("Daily list not found")
    driver.quit()
    exit()

cards = daily_list.select("div.daily-list-item")
print(f"Found {len(cards)} forecast days")
