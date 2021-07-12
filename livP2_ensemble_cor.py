# -*- coding: utf-8 -*-
from typing import List, Any, Union

import requests
from bs4 import BeautifulSoup, ResultSet
import pandas as pd


base_url = 'https://books.toscrape.com'
reponse = requests.get(base_url)

liensCat = []
links = []
page_url = []
UPC = []
titre = []
price_in = []
price_ex = []
available = []
descrip = []
cat = []
rating = []
image = []

if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        for category in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
                categories = category.a.get('href').replace('/index.html', '')
                liensCat.append('https://books.toscrape.com/' + categories)
with open('url_cat.csv', 'w') as file:
        for categories in liensCat:
                file.write(categories + '\n')


with open('url_cat.csv', 'r') as fichier :
        for row in fichier :
            url_cat = row.strip()
            reponse_cat = requests.get(url_cat)
            if reponse_cat.ok:
                soup = BeautifulSoup(reponse_cat.text, 'html.parser')
                articles = soup.findAll('article')
                for article in articles:
                    a = article.find('a')
                    link = a['href'].replace('../../../', '')
                    links.append('https://books.toscrape.com/catalogue/' + link)

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')


with open('urls.csv', 'r') as inf:
            for row in inf:
                url_livre = row.strip()
                reponse_livre = requests.get(url_livre)
                if reponse_livre.ok:
                    soup = BeautifulSoup(reponse_livre.text, 'html.parser')
                    page_url.append(url_livre)
                    UPC.append(soup.find_all('td')[0].text)
                    titre.append(soup.find('h1').text)
                    price_in.append(soup.find_all('td')[3].text.replace('Â', ''))
                    price_ex.append(soup.find_all('td')[2].text.replace('Â', ''))
                    available.append(soup.find_all('td')[5].text.replace('In stock (', '').replace('available)', ''))
                    descrip.append(soup.find_all('p')[3].text)
                    cat.append(soup.find_all('a')[3].text)
                    rating.append(soup.find("p", attrs={'class': 'star-rating'}).get("class")[1])
                    image.append(soup.find('img')['src'].replace('../../', 'https://books.toscrape.com/'))
            df = pd.DataFrame.from_dict(
                {"lien":page_url,  "universal_product_code": UPC, "Title": titre, "price_including_tax": price_in,
                "price_excluding_tax": price_ex, "number_available": available, "product_description": descrip,
                "category": cat, "review_rating": rating, " image_url": image})
            #print(df)
            df.to_csv('Livre.csv', index=False)


