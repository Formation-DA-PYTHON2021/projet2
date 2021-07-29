# -*- coding: utf-8 -*-
from typing import List, Any, Union

import requests
from bs4 import BeautifulSoup, ResultSet
import pandas as pd



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
url_cat = []


#Etape 1:
base_url = 'https://books.toscrape.com'
reponse = requests.get(base_url)

def category(base_url):
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        for category in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
            categories = category.a.get('href').replace('/index.html', '')
            liensCat.append('https://books.toscrape.com/' + categories)
            if liensCat:
                soup = BeautifulSoup(str(liensCat), 'html.parser')
                number_of_pages = soup.find('li', attrs={'class': 'current'})
                if number_of_pages is not None:
                    number_of_pages = int(number_of_pages.text.split('of ')[1])
                    for npage in range(1, number_of_pages + 1):
                        url_cat2 = str(liensCat) + "/page-" + str(npage) + '.html'
                        reponse_cat2 = requests.get(url_cat2)
                        soup = BeautifulSoup(reponse_cat2.text, 'html.parser')
                else:
                    liensCat
    return {}


# Etape 2
url_category = category()
reponse_cat = requests.get(url_category)

def pages_livre(url_category):
    soup = BeautifulSoup(reponse_cat.text, 'html.parser')
    articles = soup.findAll('article')
    for article in articles:
        a = article.find('a')
        link = a['href'].replace('../../../', '')
        links.append('https://books.toscrape.com/catalogue/' + link)
    return []


