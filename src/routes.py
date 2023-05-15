from flask import Flask, request, jsonify, url_for, Blueprint
from models import Character, Vehicles, Planet
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test', method=['GET'])
def testAPI():
    return jsonify('YOUR API WORKS, CONGRATS'), 200 