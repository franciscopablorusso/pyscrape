#script per scaricare file da un sito
from bs4 import BeautifulSoup as bs
import requests
import time

DOMAIN = 'https://www.example.com/' #indirizzo del dominio principale
URL = 'https://www.example.com/folder/' #indirizzo della cartella dove cercare
FILETYPE = '.' #questo comando specifica il tipo di file da cercare

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        print(file_link)
        with open(link.text, 'wb') as file:
            response = requests.get(DOMAIN + file_link)
            file.write(response.content)
            time.sleep(10) #introduce un tempo di attesa fra un file e l'altro
