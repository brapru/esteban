from flask import Blueprint, jsonify, request

from api import rpi
from api.models import Devices

proto = Blueprint('proto', __name__)

# LED State
@proto.route("/api/v1.0/device/<string:device>/state", methods=['GET'])
def getState(device):
    #device = Devices.query.filter_by(deviceName=deviceName).first_or_404()
    rpi.getState(device) 
    #return jsonify({'device': device.serialize()})

@proto.route("/api/v1.0/device/led/state/", methods=['POST'])
def setLedState():
    data = request.get_json()
    state = data["state"]

    rpi.setLedState(state) 
    
    return jsonify({'state': state})

    
@proto.route("/api/v1.0/device/stepper/state/<int:state>", methods=['POST'])
def setStepperState(state):
    data = request.get_json()
    state = data["state"]

    rpi.setStepperState(state) 
    rpi.setLedState(state)

    return jsonify({'state': state})

