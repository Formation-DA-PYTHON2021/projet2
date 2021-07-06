import requests
from bs4 import BeautifulSoup
import pandas as pd

links = []
url = 'https://books.toscrape.com/catalogue/category/books/travel_2'
reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html.parser')
    articles = soup.findAll('article')
    for article in articles:
        a = article.find('a')
        link = a['href'].replace('../../../', '')
        links.append('https://books.toscrape.com/catalogue/' + link)

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')
with open('urls.csv', 'r') as inf:
    #with open('catProd.csv', 'w',encoding='utf-8-sig') as outf:
    # outf.write('universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
            for row in inf:
                url = row.strip()
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
                    {"Title": [titre], "price_including_tax": [price_in], "universal_product_code": [UPC],
                    "price_excluding_tax": [price_ex], "number_available": [available], "product_description": [descrip],
                    "category": [cat], "review_rating": [rating], " image_url": [image]})
                #print(df)
                df.to_csv('Question2VF.csv', index=False)
#encore un problème dasn la console la boucle est prise en compte lorsqu'on vérifie avec print(df) les 11 lignes sortent.
#mais il n'y a pas les 11 lignes dans le fichier Question2VF