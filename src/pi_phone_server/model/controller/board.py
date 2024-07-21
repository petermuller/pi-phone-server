from pi_phone_server.exception.exceptions import InvalidPinError
from pi_phone_server.model.controller.gpio import get_gpio
from pi_phone_server.model.controller.pin import Pin, VALID_PINS


class Board:

    def __init__(self, is_pi: bool = True):
        self._gpio = get_gpio(is_pi)
        self._pin_map = {
            pin_id: Pin(pin_id=pin_id, gpio=self._gpio)
            for pin_id in VALID_PINS
        }

    def __del__(self):
        try:
            self._gpio.cleanup()
        except:  # noqa This runs on cleanup, so if cleanup fails, that's still fine
            pass

    def pin(self, pin_id: int):
        pin = self._pin_map.get(pin_id, None)
        if pin is None:
            raise InvalidPinError(f"Pin '{pin_id}' is not valid")
        return self._pin_map[pin_id]
