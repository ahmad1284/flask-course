from flask import Blueprint, request
from main.models import db


guiders_bp = Blueprint(
    "guiders_bp",
    __name__,
    url_prefix='/'
)

@guiders_bp.route('guiders')
def hoster():
    return {
        'response': 'This is guiders bp'
    }