from pydantic import BaseModel

from pi_phone_server.model.controller.pin import PinMode, Voltage


class PinModelBase(BaseModel):
    pass


class PinResponseBase(PinModelBase):
    pin_id: int


class PinSummaryResponse(PinResponseBase):
    mode: PinMode
    voltage: Voltage


class SetPinModeRequest(PinModelBase):
    mode: PinMode


class PinModeResponse(PinResponseBase):
    mode: PinMode


class SetPinVoltageRequest(PinModelBase):
    voltage: Voltage


class PinVoltageResponse(PinResponseBase):
    voltage: Voltage
