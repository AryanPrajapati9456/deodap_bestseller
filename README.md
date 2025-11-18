# 🛒 Deodap Bestseller Products Scraper

A Python-based web scraping project that extracts product data from the **Deodap Best-Selling Products** page using **BeautifulSoup** and **Requests**.

This script collects product details such as:
- 📝 Description  
- 💰 Price  
- ⭐ Star rating  
- 💬 Reviews  
- 🔗 Product URL  

and saves them in **CSV**, **JSON**, and **Excel** formats.

---

## 🚀 Features

✅ Scrapes multiple pages automatically  
✅ Handles missing data safely with custom `safe_text` and `safe_attr` functions  
✅ Adds `logging` for clean progress tracking and error reporting  
✅ Saves results in multiple formats (CSV, JSON, Excel)  
✅ Modular and reusable — easy to adapt for other websites

---

## ⚙️ Technologies Used

- **Python 3.x**  
- **BeautifulSoup4**  
- **Requests**  
- **Pandas**  
- **LXML**  
- **CSV / JSON / Excel**  
- **Logging**

---

## 📁 Project Structure

Deodap_Scraper/
│
├── scraper.py # Main scraper script
├── scraper.log # Logs all scraping activity
├── Deodap_bestseller2025-11-08.csv
├── Deodap_bestseller2025-11-08.json
├── deodap_bestseller.xlsx
└── README.md

---

## 🔧 How to Run

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/your-username/deodap-scraper.git
   cd deodap-scraper

## Install dependencies:

pip install requests beautifulsoup4 pandas lxml

## Run the scraper:

scraper.py

## Check your output files:

Deodap_bestsellerYYYY-MM-DD.csv

Deodap_bestsellerYYYY-MM-DD.json

deodap_bestseller.xlsx

## 🧠 How It Works

The script loops through multiple pages (page=1–9) of Deodap’s best-selling products.

For each page:

It fetches HTML using requests.

Parses the content using BeautifulSoup.

Extracts product fields using safe_text() and safe_attr() (to prevent crashes if tags are missing).

Adds delay (time.sleep(1)) to avoid overloading the server.

Finally, saves all collected data into 3 formats.

## 🧰 Logging System

All scraping activity and errors are recorded in scraper.log.

Example log output:

2025-11-08 15:32:10 - INFO - Scraping page 3 ...
2025-11-08 15:32:11 - INFO - Page 3 done. Waiting before next page...
2025-11-08 15:32:12 - ERROR - safe_attr error: 'NoneType' object has no attribute 'get'
2025-11-08 15:32:15 - INFO - ✅ CSV file saved as Deodap_bestseller2025-11-08.csv

## ⚠️ Ethical Note

This project is for learning and portfolio purposes only.
Always check a website’s robots.txt and terms of service before scraping.

## 🧑‍💻 Author

Aryan Prajapati
Python Developer • Web Scraper • Automation Engineer

GitHub: AryanPrajapati9456

## 🏁 Project Status

* ✅ Fully functional static scraper for Deodap’s bestseller section.  
* Ready for production or integration into larger automation workflows.
