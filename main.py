import requests
from bs4 import BeautifulSoup
import pandas as pd
import re  # 1. Import Regular Expressions

# --- STEP 1: SCRAPING (Creating 'df') ---
url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles, prices, stocks = [], [], []
books = soup.find_all('article', class_='product_pod')

for book in books:
    titles.append(book.h3.a['title'])
    prices.append(book.find('p', class_='price_color').text)
    stocks.append(book.find('p', class_='instock availability').text.strip())

# HERE we define 'df' | HIER definieren wir 'df'
df = pd.DataFrame({'Title': titles, 'Price': prices, 'Stock': stocks})

# --- STEP 2: CLEANING (Using 'df') ---
# This removes the 'Â', '£' and any other non-numeric character
df['Price'] = df['Price'].apply(lambda x: re.sub(r'[^\d.]', '', x)).astype(float)

# Simplify Stock status
df['Stock'] = df['Stock'].apply(lambda x: 'In Stock' if 'In stock' in x else 'Out of Stock')

# --- STEP 3: SAVE ---
df.to_csv('market_data_cleaned.csv', index=False)

print("SUCCESS! | ERFOLG!")
print(df.head())