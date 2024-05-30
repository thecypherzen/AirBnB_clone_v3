#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place


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

storage.new(Amenity(name="Television"))
storage.new(Amenity(name="WIFI"))
storage.new(Amenity(name="Car Hire"))
storage.new(Amenity(name="Swimming pool"))
'''

'''States

storage.new(State(name="Kogi"))
storage.new(State(name="Kaduna"))
storage.new(State(name="Abuja"))
storage.new(State(name="Benue"))
storage.new(State(name="Plateau"))
storage.new(State(name="Rivers"))
storage.new(State(name="Anambra"))
'''


'''Cities

storage.new(City(state_id="9dc9afec-22b5-42c2-9da9-469b25a620e5",
                 name="Port Harcourt"))
storage.new(City(state_id="9dc9afec-22b5-42c2-9da9-469b25a620e5",
                 name="Isiokpo"))
storage.new(City(state_id="1fa3f528-7253-4587-89b6-81418a2493db",
                 name="Garki"))
storage.new(City(state_id="1fa3f528-7253-4587-89b6-81418a2493db",
                 name="Kubwa"))
storage.new(City(state_id="1fa3f528-7253-4587-89b6-81418a2493db",
                 name="Maitama"))
storage.new(City(state_id="4564f3cf-7161-49b1-b83b-410ecd33b2a7",
                 name="Anyigba"))
storage.new(City(state_id="4564f3cf-7161-49b1-b83b-410ecd33b2a7",
                 name="Lokoja"))
storage.new(City(state_id="dc7c0991-d3a1-4991-b7a6-a1f00714ed16",
                 name="Jos"))
storage.new(City(state_id="dc7c0991-d3a1-4991-b7a6-a1f00714ed16",
                 name="Vom"))
storage.new(City(state_id="083c7333-bef2-4b2b-a8ce-262930878345",
                 name="Awka"))
storage.new(City(state_id="083c7333-bef2-4b2b-a8ce-262930878345",
                 name="Onitsha"))
'''


'''Places
storage.new(Place(
    city_id="026e3951-000b-49a6-806a-6ff8a9508361",
    user_id="027867a6-569b-4aab-bd19-725fbc1a19c6",
    name="Dream City"
))
storage.new(Place(
    city_id="19cf3dd6-36fc-4597-9eb9-fbc9f2c5822d",
    user_id="027867a6-569b-4aab-bd19-725fbc1a19c6",
    name="Garaku Mountains"
))
storage.new(Place(
    city_id="3737f5d2-7158-483a-9642-c90391daf202",
    user_id="2b3da38f-0a11-41dc-8420-8f1b9f89f48e",
    name="Comfy Apartment"
))
storage.new(Place(
    city_id="4cf26ba6-c2f3-44df-afb8-672fa70ab3b8",
    user_id="4a913e6a-482c-45cb-87e5-95dae9c5af5b",
    name="Juxtapoxe Luxurious"
))
storage.new(Place(
    city_id="5089f3bf-9658-43fa-91b0-6a23da259df7",
    user_id="78c19319-68d2-4465-a5ab-dfa86dc19689",
    name="Frestyle"
))
storage.new(Place(
    city_id="669176c8-2e0f-4c90-9b0b-3c68e67906ce",
    user_id="93985b3a-b862-45eb-959b-6e656fe125d9",
    name="Bluefontein"
))
storage.new(Place(
    city_id="ce90cecc-d59e-410c-95aa-fe6c3e43b0e1",
    user_id="027867a6-569b-4aab-bd19-725fbc1a19c6",
    name="Off Limits"
))
storage.new(Place(
    city_id="e93ee044-f4b8-4f72-ad38-5e7fdf8bde2a",
    user_id="027867a6-569b-4aab-bd19-725fbc1a19c6",
    name="Water Falls"
))
storage.new(Place(
    city_id="ec72df21-96d4-4ccb-91c1-79118b087bdb",
    user_id="2b3da38f-0a11-41dc-8420-8f1b9f89f48e",
    name="New Horizons"
))
storage.new(Place(
    city_id="fe1f6dc4-50c7-4365-a30b-554e309b82ee",
    user_id="4a913e6a-482c-45cb-87e5-95dae9c5af5b",
    name="Lake Biseria"
))
storage.new(Place(
    city_id="fe5325ef-3a18-40f6-8576-ea7d21bbb40c",
    user_id="78c19319-68d2-4465-a5ab-dfa86dc19689",
    name="Floating Gardens"
))
storage.new(Place(
    city_id="026e3951-000b-49a6-806a-6ff8a9508361",
    user_id="93985b3a-b862-45eb-959b-6e656fe125d9",
    name="Dams of Life Apartments"
))
'''

storage.save()
storage.close()
