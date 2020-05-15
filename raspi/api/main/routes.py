from flask import Blueprint, jsonify, request, render_template
from flask_socketio import SocketIO, emit

from api import socketio, rpi, scale_thread, scale_stop_event
from api.models import Devices
from api.main.utils import sendWeightToClient

main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/scale')
def scale():
    global scale_thread
    #if not scale_thread.isAlive():
    scale_thread = socketio.start_background_task(sendWeightToClient)
