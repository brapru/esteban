import time

from threading import Thread, Event
from api import rpi, socketio, pour_stop_event
from utils import get_hx_weight, get_tempsensor


class Pour:
    def __init__(self, weight):
        self.t_temp = 150
        self.weight = weight
        self.message = "starting a fresh brew"
        self.timer = ""

        self.thread = Thread()
        self.event = Event()

        self.data = {
                "message": self.message,
                "temperature": get_tempsensor(),
                "weight": get_hx_weight(),
                "timer": self.timer
            }

    def update_pour_data(self):
        self.data = {
                "message": self.message,
                "temperature": get_tempsensor(),
                "weight": get_hx_weight(),
                "timer": self.timer,
            }
        return self.data

    def emit_pour_data(self):
        while not self.event.isSet():
            data = self.update_pour_data()
            socketio.emit('pour_update', data, namespace='/pour')
            socketio.sleep(.2)

    def emit_timer(self, seconds):
        count = 0
        while count != seconds:
            socketio.emit('timer', seconds, namespace='/timer')
            seconds -= 1
            time.sleep(1)

        time.sleep(1)
        socketio.emit('timer', "", namespace='/timer')

    def set_client_message(self, message):
        self.message = message

    def boil_water(self):
        self.set_client_message("heating")
        time.sleep(3)
        rpi.boiler_on()

        while self.t_temp > get_tempsensor():
            continue

        rpi.boiler_off()

    def bloom(self):
        self.set_client_message("starting")
        time.sleep(3)
        rpi.pump_on()

        # 2g Coffee : 1g Water
        t_weight = 2 * self.weight

        while t_weight > get_hx_weight():
            continue

        self.set_client_message("blooming")
        time.sleep(3)
        rpi.pump_off()
        self.emit_timer(20)

    def brew(self):
        self.set_client_message("brewing")

        rpi.pump_on()

        t_weight = 600
        while t_weight > get_hx_weight():
            continue

        self.set_client_message("cheers")
        rpi.pump_off()

    def pour(self):
        self.thread = socketio.start_background_task(self.emit_pour_data)
        time.sleep(3)

        if self.t_temp > get_tempsensor():
            self.boil_water()

        self.bloom()
        self.brew()

        time.sleep(3)
        self.event.set()
