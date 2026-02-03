from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    url = "https://owasp.org/Top10/2021/"
    print(f"Navigating to {url}")
    driver.get(url)

    time.sleep(5)

    # ✅ These links DEFINITELY exist on this page
    vuln_links = driver.find_elements(
        By.XPATH,
        "//a[contains(@href, 'A0') or contains(@href, 'A10')]"
    )

    results = []
    seen = set()

    for link in vuln_links:
        title = link.text.strip()
        href = link.get_attribute("href")

        if title.startswith("A") and title not in seen:
            results.append({
                "Vulnerability": title,
                "Link": href
            })
            seen.add(title)

        if len(results) == 10:
            break

    print("\nTop 10 OWASP Vulnerabilities:")
    for v in results:
        print(v)

    with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Vulnerability", "Link"])
        writer.writeheader()
        writer.writerows(results)

    print("\nowasp_top_10.csv created successfully.")

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
