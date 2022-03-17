from flask import Blueprint, request
from main.models import db, Transports


transport_bp = Blueprint(
    "transport_bp",
    __name__,
    url_prefix='/'
)


@transport_bp.route('/register-transport', methods=['POST'])
def register_transports():
    transport_data = request.get_json()
    try:
        my_transport = Transports(
            transport_type = transport_data.get('transport_type'),
            rent_fee = transport_data.get('rent_fee'),
            location = transport_data.get('location'),
            phone = transport_data.get('phone')
        )
        db.session.add(my_transport)
        db.session.commit()
        return {
            'response': {
                'transport_id': my_transport.id,
                'message' : "Transport registered succesfully"
            }
        }
    except Exception as bug:
        print(bug)
        return {
            "response" : "Transport registration failed"
        }

@transport_bp.route('/get-all-transports', methods=['GET'])
def get_all_transports():
    all_transports = Transports.query.all()
    cleaned_transports = []
    for _transport in all_transports:
        transport_dict = {
            "id" : _transport.id,
            "location": _transport.location,
            "rent_fee" : _transport.rent_fee,
            "transport_type": _transport.transport_type,
            "phone": _transport.phone,
            "registered_on": _transport.date_created.isoformat()
        }
        cleaned_transports.append(transport_dict)
    return {
        "Transports": cleaned_transports
    }