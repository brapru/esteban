import sys
import pytest
import unittest
from unittest.mock import MagicMock, patch

sys.modules['RPi.GPIO'] = MagicMock()
sys.modules['spidev'] = MagicMock()
from pourover.pour import Pour

#@patch('loadcell.hx711.HX711')
#@pytest.fixture
#def init_pour():
#    return Pour(40)

class TestPour:
    def test_init_message(self, init_pour):
        assert 1 == 1
        #assert init_pour.message == "starting a fresh brew"
