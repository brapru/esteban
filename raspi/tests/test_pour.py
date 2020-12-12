import sys
import pytest
import unittest
from unittest.mock import MagicMock, patch

sys.modules['RPi.GPIO'] = MagicMock()
sys.modules['spidev'] = MagicMock()
sys.modules['HX711'] = MagicMock()
#from pourover.pour import Pour

#@pytest.fixture
#def init_pour():
#    return Pour(40)

class TestPour:
    def test_init_message(self):
        assert 1 == 1
        #assert init_pour.message == "starting a fresh brew"
