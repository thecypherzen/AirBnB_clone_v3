#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.amenity import Amenity



storage.new(Amenity(name="Internet"))
storage.new(Amenity(name="Swimming pool"))
storage.new(Amenity(name="Kitchen"))
storage.new(Amenity(name="Free Wifi"))
storage.new(Amenity(name="Car Rental"))
storage.new(Amenity(name="Breakfast"))
storage.new(Amenity(name="Fast food"))
storage.new(Amenity(name="Lunch"))
storage.new(Amenity(name="Dinner"))
storage.new(Amenity(name="Laundry"))
storage.new(Amenity(name="Chaffeur"))
storage.new(Amenity(name="Room service"))
storage.new(Amenity(name="Security"))
storage.new(Amenity(name="CCTV"))
storage.new(Amenity(name="Free ride"))
storage.new(Amenity(name="TV"))
storage.new(Amenity(name="Gym"))
storage.new(Amenity(name="Microwave"))
storage.new(Amenity(name="Launge"))
storage.new(Amenity(name="Wine bar"))
storage.new(Amenity(name="Bathroom"))
storage.new(Amenity(name="Warm water"))

storage.save()
storage.close()
