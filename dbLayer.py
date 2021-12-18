# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:39:06 2021

Run as the db layer first in a seperate terminal with python

@author: moazi
"""

from app import db
from app import Drinks


if __name__ == "__main__":
    db.create_all()
    drink = Drinks(name='Mexican Mule', description="Taquila, ginger beer and a jalapeno topping")
    db.session.add(drink)
    drink2 = Drinks(name='Taquila Sunrise', description="Taquila, OJ and a grendine finish")
    db.session.add(drink2)
    db.session.commit()
