from flask import request
from flask_restful import fields, Resource, reqparse, marshal_with
import json

from db import db
from models.models import Tenant

tenant_structure = {
    'name': fields.String,
    'passport_id': fields.Integer,
    'age': fields.Integer,
    'sex': fields.String,
    'city': fields.String,
    'address': fields.String,
    'room_number': fields.Integer
}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('passport_id', type=int)


class TenantsRequestHandler(Resource):
    @marshal_with(tenant_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            return Tenant.query.filter_by(passport_id=args['passport_id']).all()
        else:
            return Tenant.query.all()

    def post(self):
        data = json.loads(request.data)
        new_tenant = Tenant(**data)
        db.session.add(new_tenant)
        db.session.commit()
        return 'ok'

    def delete(self, value):
        tenant = Tenant.query.get(value)
        db.session.delete(tenant)
        db.session.commit()
        return 'ok'

    def patch(self, value):
        data = json.loads(request.data)
        tenant = Tenant.query.get(value)

        tenant.name = data.get('name')
        tenant.passport_id = data.get('passport_id')
        tenant.age = data.get('age')
        tenant.sex = data.get('sex')
        tenant.city = data.get('city')
        tenant.address = data.get('address')
        db.session.commit()
        return 'ok'
