from flask import Blueprint
from flask_restful import Api
from staff.resourse import StaffRequestHandler

api_bp_staff = Blueprint('staff', __name__)
api = Api(api_bp_staff)


api.add_resource(StaffRequestHandler, '/staff', '/staff/<value>')

