"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Vehicles, Planet
from routes import api

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
#app.register_blueprint(api, url_prefix='/api')

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

     all_users = User.query.all()
     user_serialized = [user_name.serialize() for user_name in all_users]
     return jsonify(user_serialized), 200

@app.route('/planet', methods=['GET'])
def handle_PLANETS():

    all_planets = Planet.query.all()
    planet_serialized = [planet_name.serialize() for planet_name in all_planets]
    return jsonify(planet_serialized), 200


@app.route('/vehicle', methods=['GET'])
def handle_VEHICLES():

    all_vehicles = Vehicles.query.all()
    vehicle_serialized = [vehicle_name.serialize() for vehicle_name in all_vehicles]
    return jsonify(vehicle_serialized), 200

@app.route('/character', methods=['GET'])
def handle_CHARACTER():

    all_characters = Character.query.all()
    character_serialized = [character_name.serialize() for character_name in all_characters]
    return jsonify(character_serialized), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
