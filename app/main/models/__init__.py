import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Transports(db.Model): #table
    #columns
    id = db.Column(db.Integer, primary_key=True)
    transport_type = db.Column(db.String(128), nullable=False)
    rent_fee = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    
    def __repr__(self) -> str:
        return f'<Transport {self.id}> : {self.rent_fee}'


class Guiders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    charging_fee = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    
    def __repr__(self) -> str:
        return f'<Guider {self.id}> : {self.name}'

# Places to visit
# - hoster name
# - location
# - places to visit
# - pricing
# - description
# - phone

class placesToVisit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    hoster_name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    fee = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    
    def __repr__(self) -> str:
        return f'<Place to visit {self.id}> : {self.places}'
