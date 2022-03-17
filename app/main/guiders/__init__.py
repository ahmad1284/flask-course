from flask import Blueprint, request
from main.models import db, Guiders
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
        all_guiders = Guiders.query.all()
        f_guiders = [] #filtered or converted to dict
        for guider in all_guiders:
            guider_json = {
                "name" : guider.name,
                "location": guider.location,
                "charging_fee": guider.charging_fee,
                "phone": guider.phone,
                "description" : guider.description
            }
            f_guiders.append(guider_json)
        return f_guiders
    def post(self):
        guiders_data = request.get_json()
        if guiders_data:
            try:
                guider = Guiders(
                    name=guiders_data.get('name'),
                    location=guiders_data.get('location'),
                    charging_fee=guiders_data.get('charging_fee'),
                    phone=guiders_data.get('phone'),
                    description=guiders_data.get('description')
                )

                db.session.add(guider)
                db.session.commit()

                return {
                    'response': "Guider added succesfully"
                }
                
            except Exception as bug:
                print(bug)
                return {
                    'response': "Failed adding guider data"
                }

        return {
            'response': 'Guiders data should not be empty'
        }

    def put(self):
        return {
            'response': "This is put guider"
        }

    def delete(self):
        return {
            'response': 'This delete guiders'
        }
