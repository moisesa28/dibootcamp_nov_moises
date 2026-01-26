#Exercise 4 : Scrape and Categorize News Articles from a JavaScript-Enabled News Site

# Use Selenium to navigate to a specific news section on the website.
# Extract and parse the HTML content that is dynamically loaded via JavaScript.
# Using BeautifulSoup, extract news article titles and publication dates.
# Categorize articles by their publication month (e.g., ‘January’, ‘February’, etc.).
# Print the categorized lists of articles.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/innovation/technology"
driver.get(url)

time.sleep(5)
#Scroll to Load More Articles
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


#Extract Rendered HTML & Parse with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

articles = soup.find_all("div", {"data-testid": "dundee-article"})
print(f"Found {len(articles)} articles")


#Extract Titles & Dates, Categorize by Month
articles_by_month = defaultdict(list)

for article in articles:
    try:
        # Extract title
        title_tag = article.find("h2", {"data-testid": "card-headline"})
        if not title_tag:
            continue
        title = title_tag.text.strip()

        # Extract publication date
        time_tag = article.find("time")
        if not time_tag or not time_tag.get("datetime"):
            continue

        date_str = time_tag["datetime"]  # ISO format
        month = datetime.fromisoformat(
            date_str.replace("Z", "")
        ).strftime("%B")

        articles_by_month[month].append(title)

    except Exception:
        continue


#Print Categorized Lists of Articles
for month, titles in articles_by_month.items():
    print(f"\n📅 {month}")
    for title in titles:
        print(f" - {title}")

driver.quit()

