#Mini-Project 2: Scraping “Scrape This Site” - Frames Page

# Mini-Project 2: Scraping “Scrape This Site” - Frames Page

import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By   # ✅ missing import
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.scrapethissite.com/pages/frames/"


def get_links_and_text(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    links = []
    for a in soup.select("a"):
        text = a.get_text(strip=True)
        href = a.get("href")
        if href:
            links.append({"text": text, "href": href})

    page_text = soup.get_text(" ", strip=True)
    text_preview = page_text[:300]

    return title, links, text_preview


def main():
    # 1) Start Selenium (webdriver-manager)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    time.sleep(3)

    # 2) Find frames and iframes
    frames = driver.find_elements(By.TAG_NAME, "frame")
    iframes = driver.find_elements(By.TAG_NAME, "iframe")

    all_frames = frames + iframes
    print("Frames found:", len(frames))
    print("Iframes found:", len(iframes))
    print("Total:", len(all_frames))

    results = []

    # 3) Loop through each frame/iframe
    for i, fr in enumerate(all_frames):
        print("\n--- Working on frame", i, "---")

        frame_src = fr.get_attribute("src")
        frame_id = fr.get_attribute("id")
        frame_name = fr.get_attribute("name")

        driver.switch_to.frame(fr)
        time.sleep(1)

        html = driver.page_source
        title, links, text_preview = get_links_and_text(html)

        results.append({
            "frame_index": i,
            "frame_type": "frame" if i < len(frames) else "iframe",
            "frame_id": frame_id or "",
            "frame_name": frame_name or "",
            "frame_src": frame_src or "",
            "title": title,
            "text_preview": text_preview,
            "num_links": len(links),
            "links": " | ".join([f"{x['text']} -> {x['href']}" for x in links[:10]])
        })

        # Go back to the main page
        driver.switch_to.default_content()

    # 4) Save to CSV
    output_file = "frames_data.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "frame_index", "frame_type", "frame_id", "frame_name", "frame_src",
            "title", "text_preview", "num_links", "links"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\nSaved:", output_file)

    # 5) Close browser
    driver.quit()


if __name__ == "__main__":
    main()

