from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import stmspi.stmspi as stm

db = SQLAlchemy()
rpi = stm.RpiController(0)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pourover.db'

    db.init_app(app)
    
    with app.app_context():
        from api.models import Devices
        db.create_all()

    from api.proto.routes import proto
    app.register_blueprint(proto)

    return app
