from flask import Flask
from flask_migrate import Migrate
from main.guiders import guiders_bp
from main.hosters import hosters_bp
from main.transports import transport_bp
from main.users import users_bp
from main.models import db, ma

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twende.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "sjsk(88888sks"
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    app.register_blueprint(hosters_bp)
    app.register_blueprint(guiders_bp)
    app.register_blueprint(transport_bp)
    app.register_blueprint(users_bp)
    
    return app