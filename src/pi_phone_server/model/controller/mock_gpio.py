"""
MockGPIO.py

A fake GPIO module so that board operations can proceed without
failing if not running on an actual Raspberry Pi
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
