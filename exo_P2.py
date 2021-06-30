import requests
from bs4 import BeautifulSoup

"""
# Récupérer les url de chaque page
links = []

for i in range(51):
    print(i)

    url = 'https://books.toscrape.com/catalogue/page-' + str(i) +'.html'
    reponse = requests.get(url)

    if reponse.ok :
        soup = BeautifulSoup(reponse.text, "html5lib")
        articles = soup.findAll('article')
        for article in articles :
            a = article.find('a')
            link = a['href']
            links.append('https://books.toscrape.com/catalogue/' + link)
            
with open('urls.txt','w') as file
        for link in links :
                file.write(link + '\n')

"""
"""
# Récupérer les informations demandées dans les pages
url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
reponse = requests.get(url)
if reponse.ok:

        soup = BeautifulSoup(reponse.text, 'html.parser')
        UPC = soup.find_all('td')[0].text
        titre = soup.find('h1').text
        #price_in = soup.find_all('td')[3].text.replace('Â'; '') #j'aimerai suprimé le 'Â' qui est devant
        #price_ex = soup.find_all('td')[2].text.replace('Â'; '') #j'aimerai suprimé le 'Â' qui est devant
        available = soup.find_all('td')[5].text
        descrip = soup.find_all('p')[3].text
        cat = soup.find_all('a')[3].text
        rating = soup.find_all('p', class_= 'star-rating Three') #j'aimerai récupérer juste le texte "three"
        image = soup.find('img') #je n'arrive pas à extraire juste l'url ; je ne sais pas si juste url ou image ?

""
with open('urls.text', 'r') as inf
                with open('livrable2.csv', 'w') as outf :
                        outf.write(print('product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
                        for row in outf
                                url = row.strip()
                                reponse = requests.get(url)
                                if reponse.ok:
                                        soup = BeautifulSoup(reponse.text, 'html.parser')
                                        UPC = soup.find_all('td')[0].text
                                        titre = soup.find('h1').text
                                        # price_in = soup.find_all('td')[3].text.replace('Â'; '') #j'aimerai suprimé le 'Â' qui est devant
                                        # price_ex = soup.find_all('td')[2].text.replace('Â'; '') #j'aimerai suprimé le 'Â' qui est devant
                                        available = soup.find_all('td')[5].text
                                        descrip = soup.find_all('p')[3].text
                                        cat = soup.find_all('a')[3].text
                                        rating = soup.find_all('p', class_='star-rating Three')  # j'aimerai récupérer juste le texte "three"
                                        image = soup.find('img')  # je n'arrive pas à extraire juste l'url ; je ne sais pas si juste url ou image ?
                                        file.write(links.text + ',' + UPC + ',' + titre + ',' + price_in + ',' + price_ex + ',' + available + ','+ descrip ','+ cat + ',' + rating + ',' + image + '\n')
                        print('product_page_url'+ links.text + 'universal_product_code: ' + UPC + 'title : ' + titre + 'price_including_tax : ' + price_in + 'price_excluding_tax :' + price_ex + 'number_available:' + available + 'product_description:'+ descrip 'category:'+ cat + 'review_rating:' + rating + 'image_url :' + image)

""



