import os
import requests
import time
import random
from datetime import datetime

base_url = "https://www.iac.org/sites/default/files/magazines/SA-{year}-{month:02d}.pdf"
save_dir = "iac_magazines"
os.makedirs(save_dir, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Python Crawler/1.0; +https://www.iac.org/)"
}

for year in range(2025, 2026):
    for month in range(1, 13):
        url = base_url.format(year=year, month=month)
        filename = f"SA-{year}-{month:02d}.pdf"
        filepath = os.path.join(save_dir, filename)

        try:
            print(f"Trying {url}")
            response = requests.get(url, headers=headers, timeout=10)

            if response.headers.get("Content-Type") == "application/pdf":
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Skipped: {filename} (not a PDF)")

        except requests.RequestException as e:
            print(f"Error for {filename}: {e}")

        time.sleep(random.uniform(1, 3))