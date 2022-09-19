from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url_base = 'https://lista.mercadolivre.com.br/'

produto_name = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_name)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': "andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"})


for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class','price-tag-fraction'})
    centavos = produto.find('span', attrs={'class','price-tag-cents'})

    #print(produto.prettify())
    print('Titulo do produto: ', titulo.text)
    print('Link do produto: ', link["href"])

    if (centavos):
        print(f'Preço do produto: R$:{real.text},{centavos.text}')
    else:
        print(f'Preço do produto: R$:{real.text}')
    print('\n\n')

