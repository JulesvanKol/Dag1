# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:28:31 2023

@author: jules
"""
pip install requests

import requests

print('Start api read application')


paginaresults = requests.get('https://catfact.ninja/facts')

print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["current_page"])

print(feitjes["data"][0]["fact"])

