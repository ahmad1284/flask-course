from flask import Blueprint, request
from main.models import db


hosters_bp = Blueprint(
    "hosters_bp",
    __name__,
    url_prefix='/'
)

@hosters_bp.route('hosters')
def hoster():
    return {
        'response': 'This is hosters bp'
    }