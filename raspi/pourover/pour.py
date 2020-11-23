import time

from threading import Thread, Event

from api import hx, tempsensor, rpi, socketio, pour_stop_event

class Pour:
    def __init__(self):
        self.t_temp = 70
        self.weight = self.get_weight()
        self.message = "starting a fresh brew"

        self.thread = Thread()
        self.event = Event()

        self.data = {
                "message": self.message,
                "temperature": self.get_temp(),
                "weight": self.get_weight()
            }

    def update_pour_data(self):
        self.data = {
                "message": self.message,
                "temperature": self.get_temp(),
                "weight": self.get_weight()
            }
        return self.data

    def emit_pour_data(self):
        while not self.event.isSet():
            data = self.update_pour_data()
            socketio.emit('pour_update', data, namespace='/pour')
            socketio.sleep(.2)

    def init_emit_thread(self):
        self.thread = socketio.start_background_task(self.emit_pour_data)

    def set_client_message(self, message):
        self.message = message 
    
    def get_weight(self):
        return max(0, int(hx.get_weight(5)))

    def get_temp(self):
        return tempsensor.get_water_temp() 

    def boil_water(self):
        self.set_client_message("heating up water")
        time.sleep(3)
        #rpi.boiler_on()
       
        # 70 > 67
        while self.t_temp > self.get_temp():
            continue

        self.set_client_message("finished heating up water")

    def pour(self):
        self.init_emit_thread()
        time.sleep(3)
        
        if self.t_temp > self.get_temp():
            self.boil_water()
        else:
            self.set_client_message("already at desired temp")
            time.sleep(3)

        self.set_client_message("enjoy :)")
        time.sleep(3)
        self.event.set()
