from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless
service = Service()  # Auto-detects chromedriver in PATH
driver = webdriver.Chrome(service=service, options=options)

# Visit the site
url = "http://10.151.12.97/thruk/cgi-bin/status.cgi?style=detail&s0_op=~&s0_type=search&add_default_service_filter=1&s0_value=ho%3AProbe%20QoE%20MC%20Apptv%20-%20CCUR"
driver.get(url)

# Wait for JS to load
time.sleep(3)

# Extract all links
elements = driver.find_elements(By.TAG_NAME, "a")
links = [element.get_attribute("href") for element in elements if element.get_attribute("href")]

# Save to CSV
df = pd.DataFrame(links, columns=["Links"])
df.to_csv("links.csv", index=False)

# Cleanup
driver.quit()

print("✅ Scraping complete. Links saved to links.csv")
