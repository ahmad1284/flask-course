from flask import Blueprint, request
from main.models import db, placesToVisit
from flask_restx import Resource, Api

hosters_bp = Blueprint(
    "hosters_bp",
    __name__,
    url_prefix='/'
)

hosters_api = Api(hosters_bp)


@hosters_api.route('hosters')
class hosters(Resource):
    def get(self):
        places_to_visits = placesToVisit.query.all()
        f_places_to_visits = []
        for place in places_to_visits:
            place_json = {
                "name": place.name,
                "hoster_name": place.hoster_name,
                "location": place.location,
                "fee": place.fee,
                "phone": place.phone,
                "description": place.description,
                "registered_on": place.date_created.isoformat()
            }
            f_places_to_visits.append(place_json)
        return f_places_to_visits

    def post(self):
        hosters_data = request.get_json()
        if hosters_data:
            try:
                places_to_visit = placesToVisit(
                    name=hosters_data.get('name'),
                    hoster_name=hosters_data.get('hoster_name'),
                    location=hosters_data.get('location'),
                    fee=hosters_data.get('fee'),
                    phone=hosters_data.get('phone'),
                    description=hosters_data.get('description')
                )

                db.session.add(places_to_visit)
                db.session.commit()

                return {
                    'response': "Hoster added succesfully"
                }

            except Exception as bug:
                print(bug)
                return {
                    'response': "Failed adding place data"
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
