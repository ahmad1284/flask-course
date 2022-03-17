from flask import Blueprint, request
from main.models import db
from flask_restx import Resource, Api

guiders_bp = Blueprint(
    "guiders_bp",
    __name__,
    url_prefix='/'
)

guiders_api = Api(guiders_bp)

@guiders_api.route('guiders')
class guider(Resource):
    def get(self):
        return {
            'response': 'This is guiders bp'
        }
    def post(self):
        return {
            'response': 'This post guider'
        }
    def put(self):
        return {
            'response':"This is put guider"
        }
    def delete(self):
        return {
            'response': 'This delete guiders'
        }