import streamlit as st
import pandas as pd
import json
import time
import io
from scraper import products
import logging

# Configure Streamlit page
st.set_page_config(
    page_title="Deodap Scraper",
    page_icon="🛒",
    layout="wide"
)

# Custom logging handler to display logs in Streamlit
class StreamlitHandler(logging.Handler):
    def __init__(self, container):
        super().__init__()
        self.container = container
        self.text = ""

    def emit(self, record):
        msg = self.format(record)
        self.text += msg + "\n"
        self.container.code(self.text, language="text")

st.title("🛒 Deodap Best-Seller Scraper")
st.markdown("Exclude raw scraping scripts. Use this interface to safe-scrape Deodap's best-selling products.")

# Sidebar for controls
with st.sidebar:
    st.header("Controls")
    start_btn = st.button("Start Scraping", type="primary")
    st.info("This process scrapes 9 pages of best-selling products.")

# Main area
if start_btn:
    st.header("Live Execution Feedback")
    
    # Progress indicators
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Log container
    log_expander = st.expander("Show Live Logs", expanded=True)
    with log_expander:
        log_container = st.empty()
    
    # Setup custom logging
    logger = logging.getLogger()
    handler = StreamlitHandler(log_container)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    
    try:
        # Progress callback
        def on_progress(page, total):
            progress = page / total
            progress_bar.progress(progress)
            status_text.text(f"⏳ Scraping page {page} of {total}...")
        
        # Run scraper
        data = products(progress_callback=on_progress)
        
        # Completion
        progress_bar.progress(100)
        status_text.success("✅ Scraping Completed Successfully!")
        
        # Display Data
        st.header("Scraped Data")
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        # Metrcis
        if not df.empty:
            col1, col2 = st.columns(2)
            col1.metric("Total Products", len(df))
            # Clean price for calculation (remove 'Rs. ' and commas if present)
            # This depends on the format, assuming it might be string. 
            # safe logic: try to extract numbers
            try:
                avg_price = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float).mean()
                col2.metric("Average Price", f"₹{avg_price:.2f}")
            except:
                pass

        # Download Section
        st.header("Download Results")
        col1, col2, col3 = st.columns(3)
        
        # CSV
        csv = df.to_csv(index=False).encode('utf-8')
        col1.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"deodap_bestseller_{time.strftime('%Y%m%d')}.csv",
            mime="text/csv",
        )
        
        # JSON
        json_data = json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8')
        col2.download_button(
            label="Download JSON",
            data=json_data,
            file_name=f"deodap_bestseller_{time.strftime('%Y%m%d')}.json",
            mime="application/json",
        )
        
        # Excel
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        
        col3.download_button(
            label="Download Excel",
            data=buffer.getvalue(),
            file_name=f"deodap_bestseller_{time.strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    except Exception as e:
        status_text.error(f"An error occurred: {e}")
        st.error(str(e))
    finally:
        # cleanup handler
        logger.removeHandler(handler)

else:
    # Initial State
    st.info("Click 'Start Scraping' to begin.")
