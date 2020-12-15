import sys
import pytest
import unittest
from unittest.mock import MagicMock, patch

sys.modules["spidev"] = MagicMock()
sys.modules["RPi.GPIO"] = MagicMock()
sys.modules["loadcell.hx711"] = MagicMock()
sys.modules["tempsensor.ds18b20"] = MagicMock()
from pourover.pour import Pour

@pytest.fixture
def pour():
    return Pour(40)

class TestPour:
    
    def test_init(self, pour):
        assert pour.message == "starting fresh brew"
