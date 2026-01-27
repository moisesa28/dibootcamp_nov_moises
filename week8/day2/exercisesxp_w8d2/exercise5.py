#xercise 5 : Scrape and Analyze Weather Data from a JavaScript-Enabled Weather Website

import re
from collections import Counter

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


url = "https://www.accuweather.com/en/us/attica/30607/hourly-weather-forecast/2139413"

# 1) Open the website with Selenium (because the site uses JavaScript)
options = Options()
# options.add_argument("--headless")  # leave this OFF at first so you can see the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

# 2) Wait for the page content to load
# We wait for something that exists in the hourly forecast section.
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(., 'RealFeel') or contains(., 'Chevron down')]"))
)

# 3) Get the full HTML after JavaScript finished loading
html = driver.page_source
driver.quit()

# 4) Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Convert the page into text (easier for a beginner approach)
text = soup.get_text("\n", strip=True)

# 5) Extract the data using a simple regex:
# hour (like 1 PM), temperature, condition (like Sunny), humidity (like 53%)
pattern = re.compile(
    r"(\d{1,2}\s(?:AM|PM))\s+"      # hour
    r"(-?\d+)[°º]?\s+"             # temperature
    r"RealFeel.*?Chevron down\s+"  # skip text between temp and condition
    r"([A-Za-z\s]+?)\s+"           # condition
    r".*?Humidity\s+(\d+)%"        # humidity
    , re.DOTALL
)

data = []
matches = pattern.findall(text)

for match in matches:
    hour = match[0]
    temp = int(match[1])
    condition = " ".join(match[2].split())
    humidity = int(match[3])

    row = {
        "hour": hour,
        "temp": temp,
        "condition": condition,
        "humidity": humidity
    }
    data.append(row)

# Remove duplicates (sometimes the same items show twice)
unique_data = []
seen = set()
for row in data:
    key = (row["hour"], row["temp"], row["condition"], row["humidity"])
    if key not in seen:
        seen.add(key)
        unique_data.append(row)

# 6) Print a few rows to show what we scraped
print("Rows scraped:", len(unique_data))
print("First 5 rows:")
for row in unique_data[:5]:
    print(row)

# 7) Analysis: average temperature + most common condition
temps = [row["temp"] for row in unique_data]
conditions = [row["condition"] for row in unique_data]
humidities = [row["humidity"] for row in unique_data]

avg_temp = sum(temps) / len(temps)
avg_humidity = sum(humidities) / len(humidities)

most_common_condition = Counter(conditions).most_common(1)[0][0]

print("\n--- Analysis Results ---")
print("Average temperature:", round(avg_temp, 2))
print("Most common condition:", most_common_condition)
print("Average humidity:", round(avg_humidity, 2))



