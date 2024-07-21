import pytest

from pi_phone_server.exception.exceptions import InvalidPinError, InvalidOperationError
from pi_phone_server.model.controller.gpio import get_gpio
from pi_phone_server.model.controller.pin import Pin, PinMode, Voltage


class TestPin:

    def test_invalid_pin(self):
        with pytest.raises(InvalidPinError):
            Pin(0, gpio=get_gpio(False))
            pytest.fail("Expected an InvalidPinError for wrong pin ID")

    def test_valid_pin(self):
        pin = Pin(7, gpio=get_gpio(False))
        summary = pin.get_summary()
        assert isinstance(pin, Pin)
        assert pin.mode == PinMode.INPUT == summary.mode
        assert pin.voltage == Voltage.LOW == summary.voltage

    def test_valid_pin_modes(self):
        pin = Pin(7, gpio=get_gpio(False))
        pin.mode = PinMode.OUTPUT
        assert pin.mode == PinMode.OUTPUT
        pin.mode = PinMode.INPUT
        assert pin.mode == PinMode.INPUT

    def test_set_voltage(self):
        pin = Pin(7, mode=PinMode.OUTPUT, gpio=get_gpio(False))
        pin.voltage = Voltage.HIGH
        assert pin.voltage == Voltage.HIGH
        pin.voltage = Voltage.LOW
        assert pin.voltage == Voltage.LOW

    def test_set_voltage_when_input_mode(self):
        pin = Pin(7, mode=PinMode.INPUT, gpio=get_gpio(False))
        with pytest.raises(InvalidOperationError):
            pin.voltage = Voltage.HIGH
            pytest.fail("Expected error when setting voltage on an input pin")
