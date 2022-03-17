from flask import Blueprint, request
from main.models import db, ma, placesToVisit, PlacesSchema, SPlaceSchema
from flask_restx import Resource, Api
from marshmallow import ValidationError

hosters_bp = Blueprint(
    "hosters_bp",
    __name__,
    url_prefix='/'
)

hosters_api = Api(hosters_bp)


@hosters_api.route('hosters')
class hosters(Resource):
    def get(self):
        all_places = placesToVisit.query.all()
        places_schema = PlacesSchema(many=True)
        f_places_to_visits = places_schema.dump(all_places)
        return {
            'PlacesToVisit': f_places_to_visits
        }

    def post(self):
        hosters_data = request.get_json()
        if hosters_data:
            try:
                s_places_schema = SPlaceSchema()
                places_to_visit = s_places_schema.load(hosters_data)

                db.session.add(places_to_visit)
                db.session.commit()

                return {
                    'response': "Hoster added succesfully"
                }

            except ValidationError as bug:
                print(bug)
                return {
                    'response': str(bug)
                }
        return {
            'response': "Failed adding place data"
        }

    def put(self):
        return {
            'response': "This is put place"
        }

    def delete(self):
        return {
            'response': 'This delete place'
        }
