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
        return {
            'response': "This is put guider"
        }

    def delete(self):
        return {
            'response': 'This delete guiders'
        }
