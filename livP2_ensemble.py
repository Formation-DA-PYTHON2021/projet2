# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://books.toscrape.com'
reponse = requests.get(url)


if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        l = soup.find('aside')
        cat = l.find_all('a')
        print(cat)
