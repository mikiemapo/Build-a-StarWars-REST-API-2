from flask import Flask, request, jsonify, url_for, Blueprint
from models import db, User, Character, Vehicles, Planet, Favorites
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET'])
def testAPI():
    return jsonify('YOUR API WORKS, CONGRATS'), 200  

@api.route('/user', methods=['GET'])
def handle_hello():

     all_users = User.query.all()
     user_serialized = [user_name.serialize() for user_name in all_users]
     return jsonify(user_serialized), 200

@api.route('/planet', methods=['GET'])
def handle_PLANETS():

    all_planets = Planet.query.all()
    planet_serialized = [planet_name.serialize() for planet_name in all_planets]
    return jsonify(planet_serialized), 200


@api.route('/vehicle', methods=['GET'])
def handle_VEHICLES():

    all_vehicles = Vehicles.query.all()
    vehicle_serialized = [vehicle_name.serialize() for vehicle_name in all_vehicles]
    return jsonify(vehicle_serialized), 200

@api.route('/character', methods=['GET'])
def handle_CHARACTER():

    all_characters = Character.query.all()
    character_serialized = [character_name.serialize() for character_name in all_characters]
    return jsonify(character_serialized), 200


#POST ROUTE HERE
@api.route('/character', methods=['POST'])
def add_CHARACTER():
    body = request.get_json() 
    character_list = Character(name=body['name'],haircolor=body['haircolor'],eyecolor=body['eyecolor'])
    db.session.add(character_list)
    db.session.commit()
    return 'CHARACTER WAS CREATED', 200

@api.route('/vehicle', methods=['POST'])
def add_VEHICLE():
    body = request.get_json() 
    vehicle_list = Vehicles(name=body['name'],manufacturer=body['manufacturer'],length=body['length'],passengers=body['passengers'])
    db.session.add(vehicle_list)
    db.session.commit()
    return 'VEHICLE WAS CREATED', 200

@api.route('/planets', methods=['POST'])
def add_PLANET():
    body = request.get_json() 
    planet_list = Planet(name=body['name'],climate=body['climate'],gravity=body['gravity'])
    db.session.add(planet_list)
    db.session.commit()
    return 'PLANET WAS CREATED', 200



#DELETE METHOD
@api.route('/planet/<int:id>', methods=['DELETE'])
def delete_PLANET(id):
    planet = Planet.query.get_or_404(id)
    db.session.delete(planet)
    db.session.commit()
    return 'PLANET WAS DELETED', 200

@api.route('/vehicle/<int:id>', methods=['DELETE'])
def delete_VEHICLE(id):
    vehicle = Vehicles.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return 'VEHICLE WAS DELETED', 200

@api.route('/character/<int:id>', methods=['DELETE'])
def delete_CHARACTER(id):
    character = Character.query.get_or_404(id)
    db.session.delete(character)
    db.session.commit()
    return 'CHARACTER WAS DELETED', 200

#FAVORITES
@api.route('/users/favorites', methods=['GET'])
def get_ALLFAVORITES(id):
    favorites = get_UserFav(id)
    favorites =[favorite.serialized() for favorite in favorites]
    return jsonify(favorites=favorites)


def get_UserFav(id):
    favorites = Favorites.query.all()
    if favorites is None :
        return "THERE ARE NONE"
    else:
        fav = []
        for favorite in favorites:
            if favorite.user_id == id :
                fav.apend(favorite)
        return fav 
    
@api.route('/addfavorites', methods = ['POST'])
def add_Fav():
    request_body= request.get_json()
    favorite = Favorites(
        user_id = request_body['user_id'],
        favorite_id = request_body['favorite_id'],
        favorite_type = request_body['favorite_type']
    )
    db.session.add(favorite)
    db.session.commit
    return "SUCCESFULL"
@api.route('/deletefavorites/<int:id>', methods = ['DELETE'])
def delete_Fav(id):
    Favorites.query.filter_by(id=id).delete()
    db.session.commit
    return "SUCCESFULL DELETE"


