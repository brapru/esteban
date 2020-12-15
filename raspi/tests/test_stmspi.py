import sys
import pytest
import unittest
from unittest.mock import MagicMock, patch

ON = 1
OFF = 0
BOIL_ON = 0
BOIL_OFF = 1
LOW = 0
MED = 1
HIGH = 2
CLOCK = 0
COUNTER = 1

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

    def test_get_device_status(self, rpi):
        rpi.boiler_on()
        rpi.pump_on()
        rpi.pump_speed(HIGH)
        rpi.pump_speed(COUNTER)

        expected_pump = rpi.pump
        expected_boiler = rpi.boiler

        assert rpi.getDeviceStatus(rpi.pump) == expected_pump
        assert rpi.getDeviceStatus(rpi.boiler) == expected_boiler

    def test_boiler_on(self, rpi, spidev_instance):
        rpi.boiler_on()
        assert rpi.boiler["state"] == BOIL_ON
        spidev_instance.writebytes.assert_called_with([36, 3, 58, 1, 58, 0, 255, 255, 255, 255, 255])

    def test_boiler_off(self, rpi, spidev_instance):
        rpi.boiler_off()
        assert rpi.boiler["state"] == BOIL_OFF
        spidev_instance.writebytes.assert_called_with([36, 3, 58, 1, 58, 1, 255, 255, 255, 255, 255])

    def test_pump_on(self, rpi, spidev_instance):
        rpi.pump_on()
        assert rpi.pump["state"] == ON
        spidev_instance.writebytes.assert_called_with([36, 2, 58, 1, 58, 1, 255, 255, 255, 255, 255])

    def test_pump_off(self, rpi, spidev_instance):
        rpi.pump_off()
        assert rpi.pump["state"] == OFF
        spidev_instance.writebytes.assert_called_with([36, 2, 58, 1, 58, 0, 255, 255, 255, 255, 255])

    @pytest.mark.parametrize('speed', [0, 1, 2])
    def test_pump_speed_low(self, rpi, spidev_instance, speed):
        rpi.pump_speed(speed)
        assert rpi.pump["speed"] == speed
        spidev_instance.writebytes.assert_called_with([36, 2, 58, 2, 58, speed, 255, 255, 255, 255, 255])

    @pytest.mark.parametrize('speed', [-1, 1.2, 5, "invalid speed"])
    def test_pump_speed_invalid(self, rpi, spidev_instance, speed):
        with pytest.raises(ValueError):
            rpi.pump_speed(speed)

    @pytest.mark.parametrize('direction', [CLOCK, COUNTER])
    def test_pump_direction(self, rpi, spidev_instance, direction):
        rpi.pump_direction(direction)
        assert rpi.pump["direction"] == direction
        spidev_instance.writebytes.assert_called_with([36, 2, 58, 3, 58, direction, 255, 255, 255, 255, 255])

    @pytest.mark.parametrize('direction', [-1, 2, 1.2, 5, "invalid direction"])
    def test_pump_speed_invalid(self, rpi, spidev_instance, direction):
        with pytest.raises(ValueError):
            rpi.pump_direction(direction)
