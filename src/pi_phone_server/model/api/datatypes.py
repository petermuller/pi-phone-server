from dataclasses import dataclass

from pi_phone_server.model.controller.pin import PinMode, Voltage


@dataclass
class PinSummaryResponse:
    pin_id: int
    mode: PinMode
    voltage: Voltage


@dataclass
class SetPinModeRequest:
    mode: PinMode


@dataclass
class PinModeResponse:
    pin_id: int
    mode: PinMode


@dataclass
class SetPinVoltageRequest:
    voltage: Voltage


@dataclass
class PinVoltageResponse:
    pin_id: int
    voltage: Voltage
