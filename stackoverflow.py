# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:21:01 2021
Just a test to connect to a API

@author: moazi
"""

import json
import requests

site = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
response = requests.get(site)

for each in response.json()['items']:
    if each['answer_count'] == 0:
        print(each['title'])
        print(each['link'])
        print("\n")