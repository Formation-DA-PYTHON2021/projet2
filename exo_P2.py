import requests
from bs4 import BeautifulSoup

"""

links = []

for i in range(51):
    print(i)


    url = 'https://books.toscrape.com/catalogue/page-' + str(i) +'.html'
    reponse = requests.get(url)

    if reponse.ok :
        print('Page:' + str(i))
        soup = BeautifulSoup(reponse.text, 'html5lib')
        articles = soup.findAll('article')
        for article in articles :
            a = article.find('a')
            link = a['href']
            links.append('https://books.toscrape.com/catalogue/' + link)

    print(links)

"""

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html5lib")
    universal_product_code = soup.find('tr',{'th': 'UPC'})
    print(universal_product_code)


