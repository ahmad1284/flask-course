from flask import Blueprint, request
from main.models import db, ma, Transports, TransportSchema, STransportSchema
from flask_restx import Resource, Api
from marshmallow import ValidationError

transport_bp = Blueprint(
    "transport_bp",
    __name__,
    url_prefix='/'
)

transport_api = Api(transport_bp)


@transport_api.route('transports')
class transport(Resource):

    def get(self):
        all_transports = Transports.query.all()
        transport_schema = TransportSchema(many=True)
        f_transports = transport_schema.dump(all_transports)
        return f_transports

    def post(self):
        transport_data = request.get_json()
        if transport_data:
            try:
                s_transport_schema = STransportSchema()
                transport = s_transport_schema.load(transport_data)
                db.session.add(transport)
                db.session.commit()
                return {
                    'response': {
                        'transport_id': transport.id,
                        'message': "Transport registered succesfully"
                    }
                }
            except ValidationError as bug:
                print(bug)
                return {
                    "response": str(bug)
                }
        return {
            'response': 'Transport data should not be empty'
        }
    def put(self):
        return {
            'response': "This is put transport"
        }

    def delete(self):
        return {
            'response': 'This delete transport'
        }