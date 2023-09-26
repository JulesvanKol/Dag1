# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:39:09 2023

@author: jules
"""

print('Start scraping application')

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://en.bcmtoday.com/')
print(pagina.content)

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
coinslist = heeldehtml.find('#coinslist')

print(coinslist)

spans = coinslist.find_all('span')
