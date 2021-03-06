from flask_socketio import SocketIO, emit
from api import hx, socketio, scale_stop_event, tempsensor, temp_stop_event
from utils import get_hx_weight, get_tempsensor

from random import random
from time import sleep


def sendWeightToClient():
    while not scale_stop_event.isSet():
        weight = get_hx_weight()
        socketio.emit('scale_update', weight, namespace='/scale')

        hx.power_down()
        hx.power_up()

        socketio.sleep(.5)


def sendTempToClient():
    while not scale_stop_event.isSet():
        temp = get_tempsensor()
        socketio.emit('temp_update', temp, namespace='/temp')
        socketio.sleep(.5)


def sendPourDataToClient():
    while not pour_stop_event.isSet():
        socketio.emit('pour_update', data, namespace='/pour')
        socketio.sleep(.5)
