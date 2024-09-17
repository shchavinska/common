from flask import request
from flask_restful import Resource, fields, reqparse, marshal_with
import json

from db import db
from models.models import Staff

staff_structure = {
    'name': fields.String,
    'passport_id': fields.Integer,
    'position': fields.String,
    'salary': fields.Integer
}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('passport_id', type=int)


class StaffRequestHandler(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            return Staff.query.filter_by(passport_id=args['passport_id']).all()
        else:
            return Staff.query.all()

    def post(self):
        data = json.loads(request.data)
        new_staff = Staff(**data)
        db.session.add(new_staff)
        db.session.commit()
        return 'ok'

    def delete(self, value):
        staff = Staff.query.get(value)
        db.session.delete(staff)
        db.session.commit()
        return 'ok'

    def patch(self, value):
        data = json.loads(request.data)
        staff = Staff.query.get(value)
        staff.name = data.get('name')
        staff.passport_id = data.get('passport_id')
        staff.position = data.get('position')
        staff.salary = data.get('salary')
        db.session.commit()
        return 'ok'
