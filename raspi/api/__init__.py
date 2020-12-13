from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

from threading import Thread, Event

import stmspi.stmspi as stm
from tempsensor.ds18b20 import DS18B20

def init_hx():
    from loadcell.hx711 import HX711
    hx = HX711(5,6)
    
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(-519)

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


### Initalize 
db = SQLAlchemy()
rpi = stm.RpiController(0)

scale_thread = Thread()
scale_stop_event = Event()
hx = init_hx()

temp_thread = Thread()
temp_stop_event = Event()
tempsensor = DS18B20("F") 

pour_thread = Thread()
pour_stop_event = Event()

socketio = SocketIO()
