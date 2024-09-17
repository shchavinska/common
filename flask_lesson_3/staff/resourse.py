from flask import request
from flask_restful import Resource, fields, reqparse, marshal_with
import json


class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staffs =[Staff('phoebe', 332211, 'security', 6000),
         Staff('rachel', 665544, 'receptionist', 5000),
         Staff('monica', 998877, 'cleaning lady', 5500)]


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
            for staff in staffs:
                if staff.passport_id == args['passport_id']:
                    return staff
        else:
            return staffs

    def delete(self, value):
        for staff in staffs:
            if staff.passport_id == int(value):
                staffs.remove(staff)
                return 'ok'

    def patch(self, value):
        data = json.loads(request.data)
        for staff in staffs:
            if staff.passport_id == int(value):
                staff.name = data['name']
                staff.passport_id = data['passport_id']
                staff.position = data['position']
                staff.salary = data['salary']
                return 'ok'

    def post(self):
        data = json.loads(request.data)
        staffs.append(Staff(data['name'], data['passport_id'], data['position'], data['salary']))
        return 'ok'

