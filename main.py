import os
import re
import time
import logging
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --------------------------------------------------
# AYARLAR
# --------------------------------------------------

EXCEL_FILE = "ikas-urunler.xlsx"
LINK_FILE = "urun_linkleri.txt"
OUTPUT_FILE = "output/ikas_zippo_fiyatlari.xlsx"

os.makedirs("logs", exist_ok=True)
os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

print("=" * 50)
print("ZIPPO SCRAPER BAŞLADI")
print("=" * 50)

# --------------------------------------------------
# EXCEL
# --------------------------------------------------

print("Excel okunuyor...")

df = pd.read_excel(EXCEL_FILE)

print("Toplam satır:", len(df))

# SKU sütunu (I sütunu)

sku_list = (
    df.iloc[:, 8]
      .fillna("")
      .astype(str)
      .str.strip()
)

sku_set = set(sku_list)

print("Toplam SKU:", len(sku_set))

# --------------------------------------------------
# LINKLER
# --------------------------------------------------

with open(LINK_FILE, "r", encoding="utf-8") as f:
    links = [x.strip() for x in f.readlines() if x.strip()]

links = list(dict.fromkeys(links))

print("Toplam Link:", len(links))

# --------------------------------------------------
# CHROME
# --------------------------------------------------

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    ),
    options=options
)

print("\nChrome açıldı.")

# --------------------------------------------------
# SONUÇLAR
# --------------------------------------------------

results = []

print("\nHazır.")
print("Bir sonraki bölümde ürünler okunmaya başlanacak.")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.zippo.com.tr/urun/13750/classic"

driver.get(url)

print("Sayfa açıldı.")

print("\n===== TÜM H1 =====")
for e in driver.find_elements(By.TAG_NAME, "h1"):
    print(e.text)

print("\n===== PRODUCT ID =====")
for e in driver.find_elements(By.CSS_SELECTOR, '[itemprop="productID"]'):
    print(e.text)

print("\n===== PRICE =====")
for e in driver.find_elements(By.CSS_SELECTOR, 'span'):
    txt = e.text.strip()
    if "₺" in txt or "TL" in txt:
        print(txt)

input("\nEnter'a bas...")

driver.quit()