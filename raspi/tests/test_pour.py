import sys
import pytest
import unittest
from unittest.mock import MagicMock, patch

from pourover.pour import Pour

@pytest.fixture
def init_pour():
    return Pour(40)

class TestPour:
    def test_init_message(self, init_pour):
        assert init_pour.message == "starting a fresh brew"
