from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
import json

from db import db
from models.models import Room

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
        if args['number']:
            return Room.query.filter_by(number=args['number']).all()
        elif args['status']:
            return Room.query.filter_by(status=args['status']).all()
        else:
            return Room.query.all()

    def post(self):
        data = json.loads(request.data)
        new_room = Room(**data)
        db.session.add(new_room)
        db.session.commit()
        return 'ok'

    def delete(self, value):
        room = Room.query.get(value)
        db.session.delete(room)
        db.session.commit()
        return 'ok'

    def patch(self, value):
        data = json.loads(request.data)
        room = Room.query.get(value)

        room.number = data.get('number')
        room.level = data.get('level')
        room.status = data.get('status')
        room.price = data.get('price')
        room.tenant_id = data.get('tenant_id')
        db.session.commit()
        return 'ok'
