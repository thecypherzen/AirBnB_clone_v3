#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.city import City


storage.new(City(state_id="50ce5adb-ef1c-494e-ae37-4b95d67d3060",
                 name="Garki"))
storage.new(City(state_id="50ce5adb-ef1c-494e-ae37-4b95d67d3060",
                 name="Guzape"))
storage.new(City(state_id="50ce5adb-ef1c-494e-ae37-4b95d67d3060",
                 name="Apo"))
storage.new(City(state_id="50ce5adb-ef1c-494e-ae37-4b95d67d3060",
                 name="Maitama"))
storage.new(City(state_id="50ce5adb-ef1c-494e-ae37-4b95d67d3060",
                 name="CBD"))
storage.new(City(state_id="164da99f-5463-414b-94cb-463b7b5c69ae",
                 name="Anyigba"))
storage.new(City(state_id="164da99f-5463-414b-94cb-463b7b5c69ae",
                 name="Lokoja"))
storage.new(City(state_id="164da99f-5463-414b-94cb-463b7b5c69ae",
                 name="Kabba"))
storage.new(City(state_id="a8bd605a-43f1-45fe-8d7c-84f5ffb2f86b",
                 name="Auskachi"))
storage.new(City(state_id="a8bd605a-43f1-45fe-8d7c-84f5ffb2f86b",
                 name="Dabasama"))

storage.new(City(state_id="2206f4f1-ed50-4e5f-86fa-2c9490876143",
                 name="Awka"))
storage.new(City(state_id="a8bd605a-43f1-45fe-8d7c-84f5ffb2f86b",
                 name="Ariaria"))
storage.new(City(state_id="2206f4f1-ed50-4e5f-86fa-2c9490876143",
                 name="Idemili"))

storage.new(City(state_id="fb258820-5394-4872-9d57-8ecb8ced9ed8",
                 name="Kafanchan"))
storage.save()
storage.close()
