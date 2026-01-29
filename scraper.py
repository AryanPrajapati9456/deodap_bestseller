import logging
from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import csv
import json
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scraper.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

def safe_text(parent, tag, class_name):
    try:
        element = parent.find(tag, class_=class_name)
        return element.get_text(strip=True) if element else None
    except AttributeError as e:
        logging.error(f"safe_text error: {e}")
        return None

def safe_attr(parent, tag, class_name, attr):
    try:
        element = parent.find(tag, class_=class_name)
        return element.get(attr) if element else None
    except AttributeError as e:
        logging.error(f"safe_attr error: {e}")
        return None

base_url = "https://deodap.in/collections/best-selling-products"

def products(progress_callback=None):
    all_products = []
    total_pages = 9
    for page in range(1, total_pages + 1):
        try:
            if progress_callback:
                progress_callback(page, total_pages)

            if page in [1, 2]:
                main_url = "https://deodap.in/collections/best-selling-products"
            else:
                main_url = f"https://deodap.in/collections/best-selling-products?page={page}"

            logging.info(f"Scraping page {page} ...")
            time.sleep(1)

            html_page = requests.get(main_url, headers=headers)
            soup = BeautifulSoup(html_page.text, "lxml")

            bestseller = soup.find_all("div", class_="card-coll-new card-wrapper product-card-wrapper underline-links-hover")

            for best in bestseller:
                product_description = safe_text(best, "a", "full-unstyled-link")
                product_price = safe_text(best, "span", "custom-price price-item price-item--sale price-item--last")
                product_star = safe_attr(best, "span", "jdgm-prev-badge__stars", "data-score")
                product_reviews = safe_text(best, "span", "jdgm-prev-badge__text")
                product_url = safe_attr(best, "a", "card__content", "href")

                p_url = f"https://deodap.in{product_url}" if product_url else None

                all_products.append({
                    "Description": product_description,
                    "Price": product_price,
                    "Stars": product_star,
                    "Reviews": product_reviews,
                    "Url": p_url
                })

            logging.info(f"Page {page} done. Waiting before next page...")
        except Exception as e:
            logging.error(f"Error while scraping page {page}: {e}")
        
    return all_products

def save_csv(data):
    try:
        file_name = f"Deodap_bestseller{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Description", "Price", "Stars", "Reviews", "Url"])
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"✅ CSV file saved as {file_name}")
    except Exception as e:
        logging.error(f"Error saving CSV: {e}")

def save_json(data):
    try:
        file_name = f"Deodap_bestseller{datetime.now().strftime('%Y-%m-%d')}.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"✅ JSON file saved as {file_name}")
    except Exception as e:
        logging.error(f"Error saving JSON: {e}")

def save_excel(data):
    try:
        df = pd.DataFrame(data)
        df.to_excel("deodap_bestseller.xlsx", index=False)
        logging.info("✅ Excel file saved as deodap_bestseller.xlsx")
    except Exception as e:
        logging.error(f"Error saving Excel: {e}")

if __name__ == "__main__":
    logging.info("🚀 Scraper started.")
    data = products()
    save_csv(data)
    save_json(data)
    save_excel(data)
    logging.info("🏁 Scraper finished successfully.")
