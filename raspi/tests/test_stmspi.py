import sys
import pytest
import unittest
from unittest.mock import MagicMock, patch

ON = 1
OFF = 0
BOIL_ON = 0
BOIL_OFF = 1

sys.modules["spidev"] = MagicMock()
from stmspi.stmspi import RpiController

@pytest.fixture
def rpi():
    return RpiController(0)

class TestRpiController:
    def test_init(self, rpi):
        assert rpi.led == { "id" : 1, "state" : OFF }
        assert rpi.pump == { "id" : 2, "state" : OFF, "direction" : 0, "speed" : 0 }
        assert rpi.boiler == { "id" : 3, "state" : OFF }

    def test_get_device_status(self, rpi):
        assert rpi.getDeviceStatus(rpi.led) == { "id" : 1, "state" : OFF }
        assert rpi.getDeviceStatus(rpi.pump) == { "id" : 2, "state" : OFF, "direction" : 0, "speed" : 0 }
        assert rpi.getDeviceStatus(rpi.boiler) == { "id" : 3, "state" : OFF }

        rpi._setDeviceState(rpi.led, ON)
        rpi._setDeviceState(rpi.pump, ON)
        rpi._setDeviceSpeed(rpi.pump, 2)
        rpi._setDeviceState(rpi.boiler, BOIL_ON)

        assert rpi.getDeviceStatus(rpi.led) == { "id" : 1, "state" : ON }
        assert rpi.getDeviceStatus(rpi.pump) == { "id" : 2, "state" : ON, "direction" : 0, "speed" : 2 }
        assert rpi.getDeviceStatus(rpi.boiler) == { "id" : 3, "state" : BOIL_ON }
    
    def test_set_device_state_boiler(self, rpi):
        with pytest.raises(ValueError):
            assert rpi._setDeviceState(rpi.boiler, 2)
        
        rpi._setDeviceState(rpi.boiler, BOIL_OFF)
        assert rpi.boiler == { "id" : 3, "state" : BOIL_OFF }

        rpi._setDeviceState(rpi.boiler, BOIL_ON)
        assert rpi.boiler == { "id" : 3, "state" : BOIL_ON }
   
    def test_set_device_speed_pump(self, rpi):
        rpi._setDeviceSpeed(rpi.pump, 2)
        assert rpi.pump["speed"] == 2

    def test_set_device_speed_not_pump(self, rpi):
        with pytest.raises(AssertionError):
            assert rpi._setDeviceSpeed(rpi.boiler, 2)

    def test_boiler_on(self, rpi):
        rpi.boiler_on()
        assert rpi.boiler["state"] == BOIL_ON

    def test_boiler_off(self, rpi):
        rpi.boiler_off()
        assert rpi.boiler["state"] == BOIL_OFF
   
    def test_pump_on(self, rpi):
        rpi.pump_on()
        assert rpi.pump["state"] == ON

    def test_pump_off(self, rpi):
        rpi.pump_off()
        assert rpi.pump["state"] == OFF
