from flask_socketio import SocketIO, emit
from api import hx, socketio, rpi, scale_thread, scale_stop_event

from random import random
from time import sleep

def sendWeightToClient():
    while not scale_stop_event.isSet():
            weight = max(0, int(hx.get_weight(5)))
            socketio.emit('scale_update', weight, namespace='/scale')
            
            hx.power_down()
            hx.power_up()
            
            socketio.sleep(.5) 
