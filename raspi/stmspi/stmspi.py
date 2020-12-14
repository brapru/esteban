import spidev
import struct

ON = 1
OFF = 0
BOIL_ON = 0
BOIL_OFF = 1

class RpiController:
    STATE = 1
    SPEED = 2
    DIR = 3

    UPDATE       = bytes("$","utf-8")
    INFO         = bytes("*","utf-8")
    SEPARATOR    = bytes(":","utf-8")

    def __init__(self, channel):
        self.spi = spidev.SpiDev()
        self.spi.open(0, channel)
        self.spi.max_speed_hz = 10000

        self.led            = { "id" : 1, "state" : 0 }
        self.pump           = { "id" : 2, "state" : 0, "direction" : 0, "speed" : 0 }
        self.boiler         = { "id" : 3, "state" : 0 }

    def _prepareToSend(self, data):
        command_data = bytearray(data)
        while len(command_data) != 11:
            command_data.append(0xFF)
        
        return command_data

    def _createCommand(self, cmdtype, device, setting, update):
        data = struct.pack('<cBcBcB', cmdtype, device, self.SEPARATOR, setting, self.SEPARATOR, update)
        
        return self._prepareToSend(data) 

    def _spiRead(self, msg_len):
        msg = self.spi.readbytes(msg_len)
        print(msg)

    def _spiWrite(self, cmd):
        self.spi.writebytes(list(cmd))
        print(cmd)
        print(list(cmd))

    def _sendToMCU(self, cmdtype, device, setting, update):
        cmd = self._createCommand(cmdtype, device, setting, update)
        self._spiWrite(cmd)

    def getDeviceStatus(self, device):
        return device

    def _setDeviceState(self, device, updated_state):
        if updated_state != 0 and updated_state != 1:
            raise ValueError("Invalid state. Device can only be ON(1) OR OFF(0)")
        
        device.update(state=updated_state)
        self._sendToMCU(self.UPDATE, device["id"], self.STATE, device["state"])
    
    def _setDeviceDirection(self, device, updated_direction):
        if device["id"] != self.pump["id"]:
            raise AssertionError("Invalid device. Device does not have attribute: direction")
        
        if updated_direction != 0 and updated_direction != 1:
            raise ValueError("Invalid direction. Device can only be CLOCK(1) OR COUNTER(0)")
        
        device.update(direction=updated_direction)
        self._sendToMCU(self.UPDATE, device["id"], self.DIR, device["direction"])

    def _setDeviceSpeed(self, device, updated_speed):
        if device["id"] != self.pump["id"]:
            raise AssertionError("Invalid device. Device does not have attribute: speed")

        device.update(speed=updated_speed)
        self._sendToMCU(self.UPDATE, device["id"], self.SPEED, device["speed"])

    def boiler_on(self):
        self._setDeviceState(self.boiler, BOIL_ON)

    def boiler_off(self):
        self._setDeviceState(self.boiler, BOIL_OFF)

    def pump_on(self):
        self._setDeviceState(self.pump, ON)
    
    def pump_off(self):
        self._setDeviceState(self.pump, OFF)
