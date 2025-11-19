import pytest

from typing import Any, Type, Dict, Optional

from pi_phone_server.model.api.datatypes import (
    PinModelBase,
    PinResponseBase,
    PinSummaryResponse,
    SetPinModeRequest,
    PinModeResponse,
    SetPinVoltageRequest,
    PinVoltageResponse
)
from pi_phone_server.model.controller.pin import PinMode, Voltage

class TestDatatypes:

    @staticmethod
    def assert_object_creation(cls: Type, cls_params: Optional[Dict[str, Any]] = None):
        if not cls_params:
            cls_params = {}
        try:
            cls(**cls_params)
        except:
            pytest.fail(f"Failed to create object of class {cls.__name__}")

    def test_create_pin_model_base(self):
        self.assert_object_creation(PinModelBase)

    def test_create_pin_response_base(self):
        self.assert_object_creation(PinResponseBase, {"pin_id": 0})

    def test_create_pin_summary_response(self):
        self.assert_object_creation(PinSummaryResponse, {
            "pin_id": 0,
            "mode": PinMode.OUTPUT,
            "voltage": Voltage.LOW
        })

    def test_create_set_pin_mode_request(self):
        self.assert_object_creation(SetPinModeRequest, {"mode": PinMode.OUTPUT})

    def test_create_pin_mode_response(self):
        self.assert_object_creation(PinModeResponse, {
            "pin_id": 0,
            "mode": PinMode.OUTPUT
        })

    def test_create_set_pin_voltage_request(self):
        self.assert_object_creation(SetPinVoltageRequest, {"voltage": Voltage.LOW})

    def test_create_pin_voltage_response(self):
        self.assert_object_creation(PinVoltageResponse, {
            "pin_id": 0,
            "voltage": Voltage.LOW
        })
