#!/usr/bin/python3
"""Creates a view for Place objects that handles all
 default RESTFul API actions
"""

from api.v1.views import app_views
from flask import abort, json, request, Response
import models
from models import storage


Place = models.place.Place
City = models.city.City
User = models.user.User
State = models.state.State
Amenity = models.amenity.Amenity


@app_views.route('/cities/<city_id>/places', strict_slashes=False)
def get_all_places(city_id):
    """Retrieves a list of all Place objects of a City:
    GET /api/v1/cities/<city_id>/places

    - If the city_id is not linked to any City object, raises a 404 error
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = []
    if len(city.places):
        for place in city.places:
            places.append(place.to_dict())
    res = json.dumps(places, indent=2) + '\n'
    return Response(res, mimetype="application/json")


@app_views.route('/places/<id>', strict_slashes=False)
def get_place(id):
    """Retrieves a single Place object: GET /api/v1/places/<place_id>

    If the place_id is not linked to any User object, raises a 404 error
    """
    place = storage.get(Place, id)
    if not place:
        abort(404)
    res = json.dumps(place.to_dict(), indent=2) + '\n'
    return Response(res, mimetype="application/json")


@app_views.route('/places/<id>', methods=['DELETE'], strict_slashes=False)
def delete_place(id):
    """Deletes a Place object: DELETE /api/v1/places/<place_id>

     - If the place_id is not linked to any Amenity object,
       +raises a 404 error
     - Returns an empty dictionary with the status code 200
    """
    place = storage.get(Place, id)
    if place is not None:
        place.delete()
        storage.save()
        storage.reload()
        res = json.dumps({}) + '\n'
        return Response(res, mimetype="application/json")
    abort(404)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a new Place: POST /api/v1/cities/<city_id>/places

    - uses request.get_json from Flask to transform the HTTP body
      + request to a dictionary
    - If the HTTP body request is not valid JSON, raises a
      +400 error with the message Not a JSON
    - If the dictionary doesn’t contain the key 'user_id', raises a 400 error
      +with the message 'Missing user_id'
    - If the dictionary doesn't contain the key 'name', raises a
      + 400 errow with the message 'Missing name'
    - If the user_id is not linked to any User object, raise a 404 error
    - Returns the new Place with the status code 201
    """
    # check if data is sent and is json
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            abort(400, description="Not a JSON")
    except Exception:
        abort(400, description="Not a JSON")
    if not data or not len(data):
        abort(400, description="Missing data")

    # check if data has compulsory attributes
    if not data.get("user_id"):
        abort(400, description="Missing user_id")
    if not data.get("name"):
        abort(400, description="Missing name")

    # check if user_id is valid
    if not storage.get(User, data.get('user_id')):
        abort(404)

    # check if a valid city
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    # create new place
    new_place = Place(
        city_id=city_id,
        name=data.get('name'),
        user_id=data.get('user_id'),
    )

    # save and return
    new_place.save()
    res = json.dumps(new_place.to_dict(), indent=2) + '\n'
    return Response(res, mimetype="application/json", status=201)


@app_views.route('/places/<string:id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(id):
    """Updates an Place object: PUT /api/v1/places/<place_id>

    - If the place_id is not linked to any Place object, raise a 404 error
    - must use request.get_json from Flask to transform the HTTP body
      +request to a dictionary
    - If the HTTP body request is not valid JSON, raise a 400
      +error with the message 'Not a JSON'
    - Updates the Place object with all key-value pairs of the dictionary.
    - Ignores keys: id, user_id, city_id, created_at and updated_at
    - Returns the User object with the status code 200
    """
    # check data is valid json and not empty
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            abort(400, description="Not a JSON")
    except Exception:
        abort(400, description="Not a JSON")
    if not data or not len(data):
        abort(400, description="Missing data")

    # get place and assign attributes
    place = storage.get(Place, id)
    if not place:
        abort(404)
    if data.get('name'):
        setattr(place, 'name', data['name'])
    if data.get('description'):
        setattr(place, 'description', data['description'])
    if data.get('number_rooms'):
        setattr(place, 'number_rooms', int(data['number_rooms']))
    if data.get('number_bathrooms'):
        setattr(place, 'number_bathrooms', int(data['number_bathrooms']))
    if data.get('max_guest'):
        setattr(place, 'max_guest', int(data['max_guest']))
    if data.get('price_by_night'):
        setattr(place, 'price_by_night', int(data['price_by_night']))
    if data.get('latitude'):
        setattr(place, 'latitude', int(data['latitude']))
    if data.get('longitude'):
        setattr(place, 'longitude', int(data['longitude']))

    place.save()
    res = json.dumps(place.to_dict(), indent=2) + '\n'
    return Response(res, mimetype="application/json")


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_places():
    """Allows a search for Place object: POST /api/v1/places_search

    - Retrieves all Place objects depending of the JSON in the body of the
      request.The JSON can contain 3 optional keys:

      states: list of State ids
      cities: list of City ids
      amenities: list of Amenity ids

      Search rules:
      - If the HTTP body request is not valid JSON, raise a 400
        +error with the message 'Not a JSON'
      - If the JSON body is empty or each list of all keys are empty: retrieve
        +all Place objects
      - If states list is not empty, results should include all Place objects
        +for each State id listed
      - If cities list is not empty, results should include all Place objects
        +for each City id listed
      - Keys states and cities are inclusive. Search results should include
        +all Place objects in storage related to each City in every State
        +listed in states, plus every City listed individually in cities,
        +unless that City was already included by states.
    """
    # check response body is valid json
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            abort(400, description="Not a JSON")
    except Exception:
        abort(400, description="Not a JSON")

    states = data.get("states")
    cities = data.get("cities")
    amenities = data.get("amenities")

    # print("about to enter")
    if not all([data, states, cities, amenities]):
        results = set(storage.all(Place).values())
    else:
        results = set()
        if states:
            for state_id in states:
                state = storage.get(State, state_id)
                if state:
                    for city in state.cities:
                        results.update({place for place in city.places})
        # for i in results:
            # print("\n",i.to_dict())
        if cities:
            for city_id in cities:
                city = storage.get(City, city_id)
                if city:
                    results.update({place for place in city.places})
        # for i in results:
        #    print("\n",i.to_dict())

    # filter results based on amenities
    # print([place.to_dict() for place in results])
    if amenities:
        # print("checking Amenities")
        amenities = [storage.get(Amenity, a_id) for a_id in amenities]
        amenities = list(filter(lambda x: x, amenities))
        amenity_ids = [amenity.id for amenity in amenities]
        if amenity_ids:
            # print("amenity ids: ", amenity_ids)
            temp_places = results.copy()
            for place in temp_places:
                if not place.amenities:
                    # print("\nplace ", place.name, "has no amenities")
                    results.discard(place)
                else:
                    p_amenity_ids = [amen.id for amen in place.amenities]
                    # print("\nplace: ", place.name, "has: ", p_amenity_ids)
                    for amenity_id in amenity_ids:
                        if amenity_id not in p_amenity_ids:
                            # print(f"discarding place: {place.name}")
                            results.discard(place)
    results = [place.to_dict() for place in results]
    for place in results:
        if place.get("amenities"):
            del place["amenities"]
    res = json.dumps(results, indent=2) + '\n'
    return Response(res, mimetype="application/json")
