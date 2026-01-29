# Task 3 & Task 4: Extract book data from Durham County Library

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import json
import time

# -------------------------------
# Setup WebDriver
# -------------------------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# -------------------------------
# Load page
# -------------------------------
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)
time.sleep(6)

# -------------------------------
# Find search result items
# -------------------------------
results_li = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
print("Total results found:", len(results_li))

results = []

# -------------------------------
# Extract data safely
# -------------------------------
for li in results_li:
    # ---- Title (always exists)
    try:
        title = li.find_element(By.CSS_SELECTOR, "span.title-content").text.strip()
    except:
        title = ""

    # ---- Authors (may be missing)
    author_elements = li.find_elements(By.CSS_SELECTOR, "a.author-link")
    authors = "; ".join(a.text.strip() for a in author_elements)

    # ---- Format & Year (may be missing)
    try:
        format_year = li.find_element(By.CSS_SELECTOR, "span.format-info").text.strip()
    except:
        format_year = ""

    # ---- Append result (IMPORTANT: always append)
    results.append({
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    })

# -------------------------------
# Create DataFrame
# -------------------------------
df = pd.DataFrame(results)
print(df)

# -------------------------------
# Task 4: Write output files
# -------------------------------
df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# -------------------------------
# Cleanup
# -------------------------------
driver.quit()
