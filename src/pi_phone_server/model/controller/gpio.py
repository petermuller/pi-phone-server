"""
gpio.py

Implements a fake GPIO module so that board operations can proceed without
failing if not running on an actual Raspberry Pi, otherwise imports the
GPIO library and initializes it
"""


class GPIO:

    BOARD = "board"

    @staticmethod
    def setmode(*args, **kwargs):
        pass

    @staticmethod
    def setup(*args, **kwargs):
        pass

    @staticmethod
    def input(*args, **kwargs):
        return 0

    @staticmethod
    def output(*args, **kwargs):
        pass

    @staticmethod
    def cleanup(*args, **kwargs):
        pass


def get_gpio(is_pi: bool = True):
    if is_pi:
        import RPi.GPIO  # noqa This won't exist outside of an actual Raspberry Pi
        RPi.GPIO.setmode(RPi.GPIO.BOARD)  # Using board numbering instead of BCM numberings
        return RPi.GPIO
    return GPIO()
