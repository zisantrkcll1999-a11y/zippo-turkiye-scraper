import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://www.zippo.com.tr/urunler/cakmak/windproof"

headers = {
    "User-Agent": "Mozilla/5.0"
}

tum_linkler = set()

for page in tqdm(range(1, 80), desc="Sayfalar Taranıyor"):

    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}?p={page}"

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print(f"Hata: Sayfa {page}")
        continue

    soup = BeautifulSoup(r.text, "lxml")

    urunler = soup.select("li.grid__item")

    for urun in urunler:

        a = urun.select_one("a")

        if a and a.get("href"):

            link = a["href"]

            if link.startswith("/"):
                link = "https://www.zippo.com.tr" + link

            tum_linkler.add(link)

print("\n=========================")
print("Toplam Benzersiz Ürün:", len(tum_linkler))

with open("urun_linkleri.txt", "w", encoding="utf-8") as f:
    for link in sorted(tum_linkler):
        f.write(link + "\n")

print("urun_linkleri.txt oluşturuldu.")