#Mini Project 1: Scraping Data from a Dynamic Webpage
# In this mini-project, you will learn how to scrape data from a dynamic 
# webpage using Selenium and BeautifulSoup. We will scrape data from a publicly 
# available dynamic webpage that allows scraping.


#Initialize Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up
from bs4 import BeautifulSoup
import requests

#Load the Web Page
options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options) 

url = "https://www.inmotionhosting.com/"
driver.get(url)


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "imh-rostrum-card")))

# Get rendered HTML
soup = BeautifulSoup(driver.page_source, "html.parser")
cards = soup.find_all("div", class_="imh-rostrum-card")

#Identify the elements that contain hosting plan details.
soup.find_all('div', class_="imh-rostrum-container")

#Extract necessary data such as plan names, features, and pricing.
plans = []
for card in cards:
    name = card.find("h3", class_="imh-rostrum-card-title")
    price = card.find('span',class_="rostrum-price")
    price_text = price.get_text(strip=True) if price else "N/A"
    if price_text == "N/A":
        continue
    
    features = [
    li.get_text(" ", strip=True)
    .replace("cPanelIncluded", "cPanel Included")
    .replace("WithcPanelor", "With cPanel or")
    for li in card.find_all("li")
]

    plans.append({
        "plan_name": name.get_text(strip=True) if name else "N/A",
        "price": price.get_text(strip=True) if price else "N/A",
        "features": " | ".join(features)
    })

#Store and Save the Data as a CSV
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(BASE_DIR, "data")
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "hosting_plans.csv")

# Write CSV (create file if it doesn't exist)
fieldnames = ["plan_name", "price", "features"]
try:
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        if plans:
            writer.writerows(plans)
    print(f"Saved {len(plans)} plans to {output_file}")
except OSError as e:
    print("Failed to write CSV:", e)


#Close the WebDriver
driver.quit()
