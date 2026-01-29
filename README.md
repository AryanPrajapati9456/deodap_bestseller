# 🛒 Deodap Bestseller Analytics & Scraper

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A professional web scraping and analytics tool designed to extract, visualize, and export data from the **Deodap Best-Selling Products** catalog. 

This project features both a **Production-Ready Python Script** for automation and a **Modern Interactive Web Interface** (built with Streamlit) for ease of use.

---

## � Project Demo




https://github.com/user-attachments/assets/51a89ce5-c619-4530-87b6-6891fe37159e


---

## �🌟 Key Features

### 🖥️ Interactive Web Dashboard
- **One-Click Scraping**: Trigger the entire process with a single button.
- **Real-Time Feedback**: View live progress bars and streaming logs as the scraper works.
- **Data Preview**: Sort and filter scraped products instantly in a responsive table.
- **Instant Export**: Download data in **CSV**, **JSON**, or **Excel** formats directly from the browser.

### ⚙️ Core Scraping Logic
- **Robust Extraction**: Custom `safe_text` and `safe_attr` handlers prevent crashes from missing data.
- **Auto-Pagination**: Automatically navigates through all bestseller pages (1-9).
- **Polished Logging**: Detailed file-based logging (`scraper.log`) for debugging and auditing.
- **Rate Limiting**: Built-in delays to respect server load and mimic human behavior.

---

## 📥 Output Data

The tool extracts the following fields for every product:
- 📝 **Product Description**
- 💰 **Price** (Current Sale Price)
- ⭐ **Star Rating**
- 💬 **Review Count**
- 🔗 **Product URL**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/AryanPrajapati9456/deodap_bestseller.git
    cd deodap_bestseller
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

#### Option A: Interactive Dashboard (Recommended)
Launch the visual interface in your browser:
```bash
streamlit run app.py
```

#### Option B: Headless CLI Scraper
Run the automation script directly in your terminal:
```bash
python scraper.py
```

---

## 📁 Project Structure

```text
├── app.py             # 🎨 Streamlit Web Application Entry Point
├── scraper.py         # 🧠 Core Scraping Logic & Data Extraction
├── scraper.log        # 📝 Runtime Logs
├── requirements.txt   # 📦 Project Dependencies
├── README.md          # 📄 Documentation
└── [Output Files]     # 📊 Generated CSV/JSON/Excel reports
```

---

## ⚠️ Ethical Considerations

This tool is designed for **educational purposes** and **personal portfolio demonstration**. 
- It respects the target site by implementing delays between requests.
- Users are responsible for adhering to `deodap.in`'s Terms of Service and `robots.txt` policy.

---

## 👤 Author

**Aryan Prajapati**
*Python Developer • Web Scraper • Automation Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-AryanPrajapati9456-181717?style=flat&logo=github)](https://github.com/AryanPrajapati9456)

---

### 📝 License
This project is open-source and available for usage under the MIT License.
