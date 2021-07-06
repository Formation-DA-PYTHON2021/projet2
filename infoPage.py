# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html.parser')
    UPC = soup.find_all('td')[0].text
    titre = soup.find('h1').text
    price_in = soup.find_all('td')[3].text.replace('Â', '')
    price_ex = soup.find_all('td')[2].text.replace('Â', '')
    available = soup.find_all('td')[5].text.replace('In stock (', '').replace('available)', '')
    descrip = soup.find_all('p')[3].text
    cat = soup.find_all('a')[3].text
    rating = soup.find("p", attrs={'class': 'star-rating'}).get("class")[1]
    image = soup.find('img')['src'].replace('../../', 'https://books.toscrape.com/')
    df = pd.DataFrame.from_dict(
        {"lien": [url], "universal_product_code": [UPC], "Title": [titre], "price_including_tax": [price_in],
         "price_excluding_tax": [price_ex], "number_available": [available], "product_description": [descrip],
         "category": [cat], "review_rating": [rating], " image_url": [image]})
    # print(df)
    df.to_csv('Question1VF.csv', index=False)
