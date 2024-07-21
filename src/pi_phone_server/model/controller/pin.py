from collections import namedtuple
from enum import IntEnum
from typing import Any

from pi_phone_server.exception.exceptions import InvalidOperationError, InvalidPinError

VALID_PINS = (7, 11, 12, 13, 15, 16, 18, 22)


class PinMode(IntEnum):
    OUTPUT = 0
    INPUT = 1


class Voltage(IntEnum):
    LOW = 0
    HIGH = 1


PinSummary = namedtuple("PinSummary", ("mode", "voltage"))


class Pin:

    def __init__(self,
                 pin_id: int,
                 gpio: Any,
                 mode: PinMode = PinMode.INPUT,
                 ):
        if pin_id not in VALID_PINS:
            raise InvalidPinError(f"Pin '{pin_id}' is not valid")
        self._gpio = gpio
        self._pin_id = pin_id
        self._mode = mode
        self._voltage = None
        self._gpio.setup(self._pin_id, self._mode)

    def get_summary(self) -> PinSummary:
        return PinSummary(
            mode=self.mode,
            voltage=self.voltage
        )

    @property
    def mode(self) -> PinMode:
        return self._mode

    @mode.setter
    def mode(self, mode: PinMode) -> None:
        self._mode = mode
        self._gpio.setup(self._pin_id, mode)

    @property
    def voltage(self) -> Voltage:
        if self.mode == PinMode.INPUT:
            self._voltage = self._gpio.input(self._pin_id)
        return self._voltage

    @voltage.setter
    def voltage(self, voltage: Voltage) -> None:
        if self.mode == PinMode.INPUT:
            raise InvalidOperationError("Cannot set voltage when pin is in INPUT mode.")
        self._gpio.output(self._pin_id, voltage)
        self._voltage = voltage
