#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
'''
storage.new(State(name="Gombe"))
storage.new(State(name="Zamfara"))
storage.save()
'''
val = storage.count(dict)
print(val)
