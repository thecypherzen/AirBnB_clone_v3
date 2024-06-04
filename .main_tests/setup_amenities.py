#!/usr/bin/python3
from models.amenity import Amenity
from models.place import Place
from models import storage
from os import getenv
from random import randint


# Amenities

pool = storage.get(Amenity, "22ed771f-2d6b-4e24-b37f-f42e93f5d62b")
wifi = storage.get(Amenity, "72724431-b4ab-493d-bd94-978235186ff5")
carhire = storage.get(Amenity, "9e0d47f9-b113-417a-94cc-97f299f49e8e")
tv = storage.get(Amenity, "b5b0adf8-3dbf-4e11-9e56-4408f4e88f7b")
ac = storage.get(Amenity, "bb0ccaaa-121e-48dd-9168-af59a22b3fb4")
generator = storage.get(Amenity, "f5a7f73f-7229-4049-9fc3-85617d57cf77")
netflix = storage.get(Amenity, "5d549b73-6025-473f-807b-47e6b3ad1020")
gym = storage.get(Amenity, "68420faa-0668-4462-92b4-f532a0e67f61")
cinema = storage.get(Amenity, "662e318d-8b7c-4cb5-8381-9dee9ade3e90")
garden = storage.get(Amenity, "578d931b-ac97-4982-b338-114aecf90125")

amenities = [pool, wifi, carhire, tv, ac, generator, netflix,
                 gym, cinema, garden]

for amenity in amenities:
    amenity.save()

# get all places
places = storage.all(Place)
_len = len(amenities)
for place in places.values():
    max_items = randint(0, _len)
    for _ in range(max_items):
        idx = randint(0, _len-1)
        if getenv('HBNB_TYPE_STORAGE') == "db":
            place.amenities.append(amenities[idx])
        else:
            place.amenity_ids.append(amenities[idx])
    place.save()
