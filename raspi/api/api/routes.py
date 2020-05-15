from flask import Blueprint, jsonify, request, render_template
from flask_socketio import SocketIO, emit

from api import socketio, rpi, scale_thread, scale_stop_event
from api.models import Devices

api = Blueprint('api', __name__)

# LED State
@api.route("/api/v1.0/device/<string:device>/state", methods=['GET'])
def getState(device):
    #device = Devices.query.filter_by(deviceName=deviceName).first_or_404()
    rpi.getState(device) 
    #return jsonify({'device': device.serialize()})

@api.route("/api/v1.0/device/led/state/", methods=['POST'])
def setLedState():
    data = request.get_json()
    state = data["state"]

    rpi.setLedState(state) 
    
    return jsonify({'state': state})

    
@api.route("/api/v1.0/device/stepper/state/<int:state>", methods=['POST'])
def setStepperState(state):
    data = request.get_json()
    state = data["state"]

    rpi.setStepperState(state) 
    rpi.setLedState(state)

    return jsonify({'state': state})


@api.route("/api/v1.0/test", methods=['GET'])
def test():
    return jsonify({'test': 'you got it dude'})
