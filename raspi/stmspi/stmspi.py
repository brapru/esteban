import spidev
import struct

class _SpiCommand:

    # Set the type of command as first byte so MCU knows what to expect
    LED = 1
    PUMP = 2
    STEPPER = 3

    STATE = 4
    SPEED = 5
    DIR = 6

    # Query the MCU to check state of device
    QUERY = 8

    # Emergency Abort Command. Halt everything.
    ABORT = 9

    def _prepareToSend(self, data):
        self.data = bytearray(data)
        self.data.append(0xFF)

    def createSetLedCommand(self, state):
        cmdType = _SpiCommand.LED
        data = struct.pack('<iB', cmdType, state) 
        self._prepareToSend(data)
    
    def createQueryCommand(self, device):
        cmdType = _SpiCommand.QUERY
        data = struct.pack('<Bs',cmdType, device)
        self._prepareToSend(data)

    """ Peristaltic Pump Command Functions """
    
    def createSetPumpStateCmd(self, state):
        cmdType = _SpiCommand.PUMP
        data = struct.pack('<iBB', cmdType, _SpiCommand.STATE, state) 
        self._prepareToSend(data)
   
    def createSetPumpSpeedCmd(self, speed):
        cmdType = _SpiCommand.PUMP
        data = struct.pack('<iBB', cmdType, _SpiCommand.SPEED, speed) 
        self._prepareToSend(data)
   
    def createSetPumpDirCmd(self, direction):
        cmdType = _SpiCommand.PUMP
        data = struct.pack('<iBB', cmdType, _SpiCommand.DIR, direction)
        self._prepareToSend(data)

class RpiController:
    
    def __init__(self, channel):
        self.spi = spidev.SpiDev()
        self.spi.open(0, channel)
        #self.spi.max_speed_hz = 10000000 
        self.spi.max_speed_hz = 10000

    def _sendCommand(self, cmd):
        self.spi.writebytes(list(cmd.data))
        print(cmd.data)
        print(list(cmd.data))

    def getState(self, device):
        cmd = _SpiCommand()
        cmd.createQueryCommand(device)
        self._sendCommand(cmd)
    
    def setLedState(self, state):
        cmd = _SpiCommand()
        cmd.createSetLedCommand(state)
        self._sendCommand(cmd)

    """ Function Calls - Peristaltic Pump """
    def setPumpState(self, state):
        cmd = _SpiCommand()
        cmd.createSetPumpStateCmd(state)
        self._sendCommand(cmd)
   
    def setPumpSpeed(self, speed):
        cmd = _SpiCommand()
        cmd.createSetPumpSpeedCmd(speed)
        self._sendCommand(cmd)

    def setPumpDirection(self, direction):
        cmd = _SpiCommand()
        cmd.createSetPumpDirCmd(direction)
        self._sendCommand(cmd)
