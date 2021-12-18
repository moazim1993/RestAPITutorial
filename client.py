# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:34:44 2021

@author: moazi
"""

import json
import requests

# add in the url
url = 'http://127.0.0.1:5000/drinks'
payload = {'name': "Jack and Coke", 'description' : "As the name suggests Jack Daneils Wiskey with Coca cola"}

if __name__ == "__main__":
    r = requests.post(url, data=json.dumps(payload))
    print(r.text)
    #data = json.dumps(payload)
    #print(data["name"])
