# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:40:22 2021
Application layer

To Run:
    1) activate the bat file in terminal
    2) Then run '$flask run'
    3) ip should be prodived by flask, connect to it
    4) ip/drinks should show the json 
@author: moazi
"""

from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# Allow 
class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return "Hello World its Mo!"

@app.route('/drinks')
def get_drinks():
    drinks = Drinks.query.all()
    out = []
    for d in drinks:
        data = {'name' : d.name, 'description' : d.description}
        out.append(data)
        
    return {'drinks' : out}

