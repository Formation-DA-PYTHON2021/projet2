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
    return liensCat

# Etape 2
url_category = 'https://books.toscrape.com/catalogue/category/books/mystery_3'

def pages_livre(url_category):
    reponse_cat = requests.get(url_category)
    if reponse_cat.ok:
        soup = BeautifulSoup(reponse_cat.text, 'html.parser')
        number_of_pages = soup.find('li', attrs={'class': 'current'})
        if number_of_pages is not None:
            number_of_pages = int(number_of_pages.text.split('of ')[1])
            for npage in range(1, number_of_pages + 1):
                url_cat2 = url_category + "/page-" + str(npage) + '.html'
                reponse_cat2 = requests.get(url_cat2)
                soup = BeautifulSoup(reponse_cat2.text, 'html.parser')
                articles = soup.findAll('article')
                for article in articles:
                    a = article.find('a')
                    link = a['href'].replace('../../../', '')
                    links.append('https://books.toscrape.com/catalogue/' + link)
        else:
            articles = soup.findAll('article')
            for article in articles:
                a = article.find('a')
                link = a['href'].replace('../../../', '')
                links.append('https://books.toscrape.com/catalogue/' + link)
    return links

#Etape 3
#Ecrire fonction Write_image(lien_image_livre, nom_categorie) qui utilise path et wget pour classer
# en fonction des parametres "lien_image_livre, nom_categorie"

#Etape 4
#Ecrire une fonction livre(lien_un_livre) qui recupere les infos du livre et appelle la fonction
#write_image(lien_image_livre, nom_categorie) et retourne les infos du livre dans un dictionnaire.

lien_un_livre = 'https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
def livre(lien_un_livre):
    reponse_livre = requests.get(lien_un_livre)
    if reponse_livre.ok:
        soup = BeautifulSoup(reponse_livre.text, 'html.parser')
        page_url.append(lien_un_livre)
        UPC.append(soup.find_all('td')[0].text)
        titre.append(soup.find('h1').text)
        price_in.append(soup.find_all('td')[3].text.replace('Â', ''))
        price_ex.append(soup.find_all('td')[2].text.replace('Â', ''))
        available.append(soup.find_all('td')[5].text.replace('In stock (', '').replace('available)', ''))
        descrip.append(soup.find_all('p')[3].text)
        cat.append(soup.find_all('a')[3].text)
        rating.append(soup.find("p", attrs={'class': 'star-rating'}).get("class")[1])
        image.append(soup.find('img')['src'].replace('../../', 'https://books.toscrape.com/'))

    return {"lien": page_url, "universal_product_code": UPC, "Title": titre, "price_including_tax": price_in,
         "price_excluding_tax": price_ex, "number_available": available, "product_description": descrip,
         "category": cat, "review_rating": rating, " image_url": image}
#attention sur la présentation le texte apparait avec encore des crochés à voir ou ça ne passe pas le .text
# plus ajout de l'étape 3 !!

#Etape 5
#Ecrire une fonction write_csv(infos_livre, nom categorie) qui ouvre un fichier csv avec pour nom
#la categorie passé en parametre, puis enregistre les infos "infos_livre" recu dans le csv.

infos_livre = {"lien": page_url, "universal_product_code": UPC, "Title": titre, "price_including_tax": price_in,
         "price_excluding_tax": price_ex, "number_available": available, "product_description": descrip,
         "category": cat, "review_rating": rating, " image_url": image}

lien_sources = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'

def write_csv(infos_livre,category):
    fieldnames = ['product_page_url', 'universal_product_code', 'title, price_including_tax', 'price_excluding_tax',
                  'number_available','product_description', 'category', 'review_rating', 'image_url']
    rows = livre()
    with open(f'{category}.csv', 'w', encoding='UTF8', newline='') as file:
        writer = f'{category}.csv'.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


#Etape 6
#Organiser toutes les fonctions dans le main du fichier.
#if __name__ == '__main__':