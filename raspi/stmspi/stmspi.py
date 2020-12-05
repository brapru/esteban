import spidev
import struct

ON = 1
OFF = 0

class RpiController:

    def __init__(self, channel):
        self.spi = spidev.SpiDev()
        self.spi.open(0, channel)
        self.spi.max_speed_hz = 10000

        self.__STATE = 1
        self.__SPEED = 2
        self.__DIR = 3

        self.__UPDATE       = bytes("$","utf-8")
        self.__INFO         = bytes("*","utf-8")
        self.__SEPARATOR    = bytes(":","utf-8")

        self.led            = { "id" : 1, "state" : 0 }
        self.peristaltic    = { "id" : 2, "state" : 0, "direction" : 0, "speed" : 0 }
        self.boiler         = { "id" : 3, "state" : 0 }

    def _prepareToSend(self, data):
        self.data = bytearray(data)
        while len(self.data) != 11:
            self.data.append(0xFF)
        print(len(self.data))

    def _createCommand(self, cmdtype, device, setting, update):
        #device = bytes(device, 'utf-8')
        data = struct.pack('<cBcBcB', cmdtype, device, self.__SEPARATOR, setting, self.__SEPARATOR, update)
        self._prepareToSend(data) 

    def _spiRead(self, msg_len):
        #msg = self.spi.xfer2(list(self.data))
        msg = self.spi.readbytes(msg_len)
        print(msg)

    def _spiWrite(self, cmd):
        self.spi.writebytes(list(self.data))
        print(self.data)
        print(list(self.data))

    def sendToMCU(self, cmdtype, device, setting, update):
        cmd = self._createCommand(cmdtype, device, setting, update)
        self._spiWrite(cmd)

    def getDeviceStatus(self, device):
        return device

    def setDeviceState(self, device, updated_state):
        if updated_state != 0 and updated_state != 1:
            raise ValueError("Invalid state. Device can only be ON(1) OR OFF(0)")
        
        device.update(state=updated_state)
        self.sendToMCU(self.__UPDATE, device["id"], self.__STATE, device["state"])
    
    def setDeviceDirection(self, device, updated_direction):
        if updated_direction != 0 and updated_direction != 1:
            raise ValueError("Invalid direction. Device can only be CLOCK(1) OR COUNTER(0)")
        
        device.update(direction=updated_direction)
        self.sendToMCU(self.__UPDATE, device["id"], self.__DIR, device["direction"])

    def setDeviceSpeed(self, device, updated_speed):
        device.update(speed=updated_speed)
        self.sendToMCU(self.__UPDATE, device["id"], self.__SPEED, device["speed"])

    def boiler_on(self):
        self.setDeviceState(self.boiler, 0)

    def boiler_off(self):
        self.setDeviceState(self.boiler, 1)

    def pump_on(self):
        self.setDeviceState(self.peristaltic, ON)
    
    def pump_off(self):
        self.setDeviceState(self.peristaltic, OFF)
