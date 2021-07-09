# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://books.toscrape.com'
reponse = requests.get(url)


if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        categories = soup.find('ul', attrs={'class': 'nav-list'}).find('li').find('ul').findAll('li')
        for category in categories:
            categories[category.text.strip()] = 'http://books.toscrape.com'/category).find('a')['href'].replace('/index.html', '')}"
        print(categories)
