# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

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

for i in range(1,8) :
    url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/page-' + str(i) + '.html'
    print(url)
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        articles = soup.findAll('article')
        for article in articles:
            a = article.find('a')
            link = a['href'].replace('../../../', '')
            links.append('https://books.toscrape.com/catalogue/' + link)
        # print(links)