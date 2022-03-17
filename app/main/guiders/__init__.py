from flask import Blueprint, request
from main.models import db, ma, Guiders, GuidersSchema, SGuidersSchema
from flask_restx import Resource, Api
from marshmallow import ValidationError

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
        guider_schema = GuidersSchema(many=True)
        # deserialize obj to text?
        f_guiders = guider_schema.dump(all_guiders)
        return f_guiders

    def post(self):
        guiders_data = request.get_json()
        if guiders_data:
            try:
                
                s_guider_schema = SGuidersSchema()
                guider = s_guider_schema.load(guiders_data)
                db.session.add(guider)
                db.session.commit()

                return {
                    'response': "Guider added succesfully"
                }

            except ValidationError as bug:
                print(bug)
                return {
                    'response': str(bug)
                }

        return {
            'response': 'Guiders data should not be empty'
        }

    def put(self):
        guider_update_data = request.get_json()
        if guider_update_data and guider_update_data.get('id'):
            _id = guider_update_data.get('id')
            try:
                target_guide = Guiders.query.filter_by(id=_id).first()
                if not target_guide:
                    return {
                        'response':"Guider ID does not exist"
                    }
                if guider_update_data.get('name'):
                    target_guide.name = guider_update_data.get('name')
                
                if guider_update_data.get('location'):
                    target_guide.location = guider_update_data.get('location')
                
                if guider_update_data.get('charging_fee'):
                    target_guide.charging_fee = guider_update_data.get('charging_fee')
                
                if guider_update_data.get('phone'):
                    target_guide.phone = guider_update_data.get('phone')
                    
                db.session.add(target_guide)
                db.session.commit()
                return {
                    'response':"guider update succesfully"
                }
            except Exception as bug:
                print(bug)
                return {
                     'response': f'Failed updating guide data with ID {_id}',
                     'error_msg': str(bug)
                }
        
        return {
            'response': "Please structure well update request"
        }

    def delete(self):
        guider_data = request.get_json()
        if guider_data and guider_data.get('id'):
            try:
                _id = guider_data.get('id')
                guider = Guiders.query.filter_by(id=_id).first()
                if not guider:
                    return {
                        'response': f"Guider with an Id of {_id} has been deleted"
                    }
                db.session.delete(guider)
                db.session.commit()
            except Exception as bug:
                print(bug)
                return {
                    'response' : f"Failed to delete guider with ID of {_id}"
                }
        return {
            'response': '400 bad request'
        }
