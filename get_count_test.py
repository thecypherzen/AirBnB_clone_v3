#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.user import User
from models.amenity import Amenity

''' Users
storage.new(User(first_name="John", last_name="Kaase",
                 email="john.k@testdb.com",
                 password="johnk123"))

storage.new(User(first_name="Good", last_name="Man",
                 email="gm@testdb.com",
                 password="gdmand230"))

storage.new(User(first_name="Claire", last_name="Bassey",
                 email="focus@testdb.com",
                 password="kldear@09"))

storage.new(User(first_name="Phoebe", last_name="Albert",
                 email="phb@testdb.com",
                 password="pa-jsd09"))

storage.new(User(first_name="Dora", last_name="Ekaji",
                 email="dk@testdb.com",
                 password="ie[ppoi"))

storage.new(User(email="john.k@testdb.com",
                 password="johnk123"))
'''

'''Amenities
'''
storage.new(Amenity(name="Television"))
storage.new(Amenity(name="WIFI"))
storage.new(Amenity(name="Car Hire"))
storage.new(Amenity(name="Swimming pool"))

storage.save()
storage.close()
