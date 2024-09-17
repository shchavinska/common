from flask import request
from flask_restful import fields, Resource, reqparse, marshal_with
import json


class Tenant:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


tenants =[Tenant('joey', 112233, 25, 'male', {'city': 'kyiv', 'street': 'khreshchatyk'}, 1),
          Tenant('chandler', 445566, 26, 'male', {'city': 'kyiv', 'street': 'poshtova ploshcha'}, 2),
          Tenant('ross', 778899, 27, 'male', {'city': 'kyiv', 'street': 'oleny teligy'}, 3)]

address_structure = {
    'city': fields.String,
    'street': fields.String
}

tenant_structure = {
    'name': fields.String,
    'passport_id': fields.Integer,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(address_structure),
    'room_number': fields.Integer
}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('passport_id', type=int)


class TenantsRequestHandler(Resource):
    @marshal_with(tenant_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            for tenant in tenants:
                if tenant.passport_id == args['passport_id']:
                    return tenant
        else:
            return tenants

    def delete(self, value):
        for tenant in tenants:
            if tenant.passport_id == int(value):
                tenants.remove(tenant)
                return 'ok'

    def patch(self, value):
        data = json.loads(request.data)
        for tenant in tenants:
            if tenant.passport_id == int(value):
                tenant.name = data['name']
                tenant.passport_id = data['passport_id']
                tenant.age = data['age']
                tenant.sex = data['sex']
                tenant.address = data['address']
                tenant.room_number = data['room_number']
                return 'ok'

    def post(self):
        data = json.loads(request.data)
        tenants.append(Tenant(data['name'], data['passport_id'], data['age'], data['sex'], data['address'], data['room_number']))
        return "ok"

