import platform
import pytest

from pi_phone_server.exception.exceptions import InvalidPinError, InvalidOperationError
from pi_phone_server.model.controller.pin import Pin, PinMode, Voltage


class TestPin:

    def test_arm_pin(self):
        if platform.machine().startswith("arm"):
            pin = Pin(7, is_pi=True)
            assert isinstance(pin, Pin)
        else:
            with pytest.raises(ModuleNotFoundError):
                Pin(7, is_pi=True)

    def test_invalid_pin(self):
        with pytest.raises(InvalidPinError):
            Pin(0)
            pytest.fail("Expected an InvalidPinError for wrong pin ID")

    def test_valid_pin(self):
        pin = Pin(7, is_pi=False)
        summary = pin.get_summary()
        assert isinstance(pin, Pin)
        assert pin.mode == PinMode.INPUT == summary.mode
        assert pin.voltage == Voltage.LOW == summary.voltage

    def test_valid_pin_modes(self):
        pin = Pin(7, is_pi=False)
        pin.mode = PinMode.OUTPUT
        assert pin.mode == PinMode.OUTPUT
        pin.mode = PinMode.INPUT
        assert pin.mode == PinMode.INPUT

    def test_set_voltage(self):
        pin = Pin(7, mode=PinMode.OUTPUT, is_pi=False)
        pin.voltage = Voltage.HIGH
        assert pin.voltage == Voltage.HIGH
        pin.voltage = Voltage.LOW
        assert pin.voltage == Voltage.LOW

    def test_set_voltage_when_input_mode(self):
        pin = Pin(7, mode=PinMode.INPUT, is_pi=False)
        with pytest.raises(InvalidOperationError):
            pin.voltage = Voltage.HIGH
            pytest.fail("Expected error when setting voltage on an input pin")
