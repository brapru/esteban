import spidev
import struct

LED_ON = 0
LED_OFF = 1

class _SpiCommand:

    # Set the type of command as first byte so MCU knows what to expect
    LED = 1
    STEPPERSPEED = 2
    STEPPERDIR = 3
    PUMPSPEED = 4
    PUMPDIR = 5

    # Query the MCU to check state of device
    QUERY = 8

    # Emergency Abort Command. Halt everything.
    ABORT = 9

    def _prepareToSend(self, data):
        self.data = bytearray(data)
        #self.data.append(0xFF)

    def createSetLedCommand(self, state):
        # BYTE STRUCTURE: TYPE - DATA
        # Turn on LED Example: 0x01 0x00
        cmdType = _SpiCommand.LED
        data = struct.pack('<BB', cmdType, state) 
        self._prepareToSend(data)

    def createSetStepperCommand(self, state):
        cmdType = _SpiCommand.LED
        data = struct.pack('<B', state) 
        self._prepareToSend(data)
    
    def createQueryCommand(self, device):
        cmdType = _SpiCommand.QUERY
        data = struct.pack('<Bs',cmdType, device)
        self._prepareToSend(data)

class RpiController:
    
    def __init__(self, channel):
        self.spi = spidev.SpiDev()
        self.spi.open(0, channel)
        self.spi.max_speed_hz = 1000000

    def _sendCommand(self, cmd):
        self.spi.writebytes(list(cmd.data))
        #print(cmd.data)

    def setLed(self, state):
        cmd = _SpiCommand()
        cmd.createSetLedCommand(state)
        self._sendCommand(cmd)

    def setStepper(self, state):
        cmd = _SpiCommand()
        cmd.createSetStepperCommand(state)
        self._sendCommand(cmd)

    def getState(self, device):
        cmd = _SpiCommand()
        cmd.createQueryCommand(device)
        self._sendCommand(cmd)
