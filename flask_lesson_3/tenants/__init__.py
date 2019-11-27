from flask import Blueprint
from flask_restful import Api
from tenants.resourse import TenantsRequestHandler

api_bp_tenants = Blueprint('tenants', __name__)
api = Api(api_bp_tenants)


api.add_resource(TenantsRequestHandler, '/tenant', '/tenant/<value>')
