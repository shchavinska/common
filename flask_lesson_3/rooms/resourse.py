from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
import json


class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms =[Room(1, 'standart', 'available', 100),
        Room(2, 'standart+', 'available', 150),
        Room(3, 'luxury', 'not available', 250)]


room_structure = {
    'number': fields.Integer,
    'level': fields.String,
    'status': fields.String,
    'price': fields.Integer
}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('number', type=int)
parser.add_argument('status', type=str)


class RoomRequestHandler(Resource):
    @marshal_with(room_structure)
    def get(self):
        args = parser.parse_args()
        room_status = []
        if args['number']:
            for room in rooms:
                if room.number == args['number']:
                    return room
        if args['status']:
            for room in rooms:
                if room.status == args['status']:
                    room_status.append(room)
            return room_status
        else:
            return rooms

    def post(self):
        data = json.loads(request.data)
        rooms.append(Room(data['number'], data['level'], data['status'], data['price']))
        return 'ok'

    def delete(self, value):
        for room in rooms:
            if room.number == int(value):
                rooms.remove(room)
                return 'ok'

    def patch(self, value):
        data = json.loads(request.data)
        for room in rooms:
            if room.number == int(value):
                room.number = data['number']
                room.level = data['level']
                room.status = data['status']
                room.price = data['price']
                return 'ok'

