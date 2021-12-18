# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:34:44 2021
client that'll connect to API
@author: moazi
"""

import json
import requests
import time

# add in the url
url = "http://127.0.0.1:5000/drinks"
#payload = {'name': "Jack and Coke",'description' : "As the name suggests Jack Daneils Wiskey with Coca cola"}
payload = {'name': "Jin and Juice",
           'description' : "London Dry Gin with your choice of lemon or lime juice"}



if __name__ == "__main__":
    r = requests.post(url, json=payload).json()
    print(r)
    r = "/" + str(r["id"])
    print("Giving 30 seconds to check the data at : ", url)
    time.sleep(30)
    print("now deleting the entry")
    delR = requests.delete(url + r)
    print(delR.text)
