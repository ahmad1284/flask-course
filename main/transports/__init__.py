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
        transport_update_data = request.get_json()
        if transport_update_data and transport_update_data.get('id'):
            _id = transport_update_data.get('id')
            try:
                target_transport = Transports.query.filter_by(id=_id).first()
                if not target_transport:
                    return {
                        'response':"Transport ID does not exist"
                    }
                if transport_update_data.get('transport_type'):
                    target_transport.transport_type = transport_update_data.get('transport_type')
                    
                if transport_update_data.get('rent_fee'):
                    target_transport.rent_fee = transport_update_data.get('rent_fee')
                    
                if transport_update_data.get('location'):
                    target_transport.location = transport_update_data.get('location')
                
                if transport_update_data.get('phone'):
                    target_transport.phone = transport_update_data.get('phone')
                    
                db.session.add(target_transport)
                db.session.commit()
                return {
                    'response':"Transport updated succesfully"
                }
            except Exception as bug:
                print(bug)
                return {
                    'response': f'Failed updating Transport data with ID {_id}'
                }
        return {
            'response': "Please structure well update request"
        }

    def delete(self):
        transport_data = request.get_json()
        if transport_data and transport_data.get('id'):
            try:
                _id = transport_data.get('id')
                transport = Transports.query.filter_by(id=_id).first()
                if not transport:
                    return {
                        'response': f"The Id {_id} does not exist"
                    }
                db.session.delete(transport)
                db.session.commit()
                return {
                    'response' : f"Place with an ID of {_id} has been deleted"
                }
            except Exception as bug:
                print(bug)
                return {
                    'response': f"Failed to delete place with ID of {_id}"
                }
        return {
            'response': '400 bad response'
        }