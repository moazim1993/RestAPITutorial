# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:40:22 2021
Application layer - main logic for API

@author: moazi
"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drinks.query.get_or_404(id)
    return {"name" : drink.name, 'description': drink.description}


@app.route('/drinks', methods=['POST'])
def add_drink():
    """
    content = request.json
    print(content)
    return {'test' : "True"}
    """
    drink = Drinks(name=request.json['name'],
                   description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id' : drink.id}
    


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drinks.query.get(id)
    if drink is None:
        return {"ERROR": "404 NOT FOUND"}
    db.session.delete(drink)
    db.session.commit()
    return {"SUCCESS" : "Drink {} is deleted".format(id)}


