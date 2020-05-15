from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

from threading import Thread, Event

import stmspi.stmspi as stm
from loadcell.hx711 import HX711

def init_hx():
    hx = HX711(5,6)
    
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(535)

    hx.reset()
    hx.tare()
    return hx

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pourover.db'

    db.init_app(app)
    
    with app.app_context():
        from api.models import Devices
        db.create_all()

    from api.main.routes import main
    from api.api.routes import api
    app.register_blueprint(main)
    app.register_blueprint(api)

    socketio.init_app(app)
    return app

db = SQLAlchemy()
rpi = stm.RpiController(0)

scale_thread = Thread()
scale_stop_event = Event()

socketio = SocketIO()

hx = init_hx()
