# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:39:06 2021

Run as the db layer first in a seperate terminal with python

@author: moazi
"""

from app import db
from app import Drinks

db.create_all()
drink = Drink(name='Coca-cola', description="Refreshing, crisp, sweet cola")
db.session.add(drink)
drink2 = Drink(name='Coca-cola', description="Refreshing, crisp, sweet cola")
