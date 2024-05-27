#!/usr/bin/python3

from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.engine import db_storage

# clear db
classes = {"User": User, "Place": Place, "State":State}
objs = storage.all()
for key, obj in objs.items():
    key = key.split('.')
    obj = storage.get(classes[key[0]], key[1])
    storage.delete(obj)

user_1 = User(
    email="user1@localhost.com",
    password="user1passwd",
    first_name="User",
    last_name="One"
)

user_2 = User(
    email="user2@localhost.com",
    password="user2passwd",
    first_name="User",
    last_name="Two"
)

storage.new(user_1)
storage.new(user_2)
storage.save()

print("Users: ", storage.count(User))
print("States ", storage.count(State))
print("Places: ", storage.count(Place))
print("Total: ", storage.count())

objs = storage.all()
print(objs)
for key, obj in objs.items():
    key = key.split('.')
    obj = storage.get(classes[key[0]], key[1])
    print("{} == {}: {}".format(
        key[1], obj.id, key[1] == obj.id
    ))
