from flask import Blueprint
from flask_restful import Api
from rooms.resourse import RoomRequestHandler

api_bp_rooms = Blueprint('rooms', __name__)
api = Api(api_bp_rooms)

api.add_resource(RoomRequestHandler, '/rooms', '/rooms/<value>')

