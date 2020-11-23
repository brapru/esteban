from flask import Blueprint, jsonify, request, render_template
from flask_socketio import SocketIO, emit

from api import socketio, rpi, scale_thread, temp_thread, pour_thread
from api.models import Devices
from api.main.utils import sendWeightToClient, sendTempToClient
from pourover.pour import Pour

main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@main.route("/pour.html", methods=['GET'])
def pour_html():
    return render_template('pour.html')

@socketio.on('connect', namespace='/scale')
def scale():
    global scale_thread
    #if not scale_thread.isAlive():
    scale_thread = socketio.start_background_task(sendWeightToClient)

@socketio.on('connect', namespace='/temp')
def scale():
    global temp_thread
    #if not scale_thread.isAlive():
    temp_thread = socketio.start_background_task(sendTempToClient)

@socketio.on('connect', namespace='/pour')
def pour():
    brew = Pour()

    global pour_thread
    pour_thread = socketio.start_background_task(brew.pour) 
