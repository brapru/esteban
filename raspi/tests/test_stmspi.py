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


@pytest.fixture
def spidev_instance():
    return sys.modules["spidev"].SpiDev()


class TestRpiController:

    def test_init(self, rpi, spidev_instance):
        assert rpi.led == {"id": 1, "state": OFF}
        assert rpi.pump == {"id": 2, "state": OFF, "direction": 0, "speed": 0}
        assert rpi.boiler == {"id": 3, "state": OFF}

        spidev_instance.open.assert_called_with(0, 0)
        assert spidev_instance.max_speed_hz == 10000

    def test_send_to_mcu(self, rpi, spidev_instance):
        rpi._sendToMCU(rpi.UPDATE, rpi.pump["id"], rpi.STATE, rpi.pump["state"])
        spidev_instance.writebytes.assert_called_with([36, 2, 58, 1, 58, 0, 255, 255, 255, 255, 255])

    def test_get_device_status(self, rpi):
        rpi._setDeviceState(rpi.led, ON)
        rpi._setDeviceState(rpi.pump, ON)
        rpi._setDeviceSpeed(rpi.pump, 2)
        rpi._setDeviceState(rpi.boiler, BOIL_ON)

        expected_led = rpi.led
        expected_pump = rpi.pump
        expected_boiler = rpi.boiler

        assert rpi.getDeviceStatus(rpi.led) == expected_led
        assert rpi.getDeviceStatus(rpi.pump) == expected_pump
        assert rpi.getDeviceStatus(rpi.boiler) == expected_boiler

    def test_set_device_state_boiler(self, rpi):
        with pytest.raises(ValueError):
            assert rpi._setDeviceState(rpi.boiler, 2)

        rpi._setDeviceState(rpi.boiler, BOIL_OFF)
        assert rpi.boiler == {"id": 3, "state": BOIL_OFF}

        rpi._setDeviceState(rpi.boiler, BOIL_ON)
        assert rpi.boiler == {"id": 3, "state": BOIL_ON}

    def test_set_device_speed_pump(self, rpi):
        rpi._setDeviceSpeed(rpi.pump, 2)
        assert rpi.pump["speed"] == 2

    def test_set_device_speed_not_pump(self, rpi):
        with pytest.raises(AssertionError):
            assert rpi._setDeviceSpeed(rpi.boiler, 2)

    def test_set_device_direction_pump(self, rpi):
        rpi._setDeviceDirection(rpi.pump, 1)
        assert rpi.pump["direction"] == 1

    def test_set_device_direction_not_pump(self, rpi):
        with pytest.raises(AssertionError):
            assert rpi._setDeviceDirection(rpi.boiler, 1)

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
