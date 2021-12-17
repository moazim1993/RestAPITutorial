# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:40:22 2021

@author: moazi
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World its Mo!"