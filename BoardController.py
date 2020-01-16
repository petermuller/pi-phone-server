#!/usr/bin/env python3
"""
BoardController.py

A class for controlling the GPIO pins on a Raspberry Pi. If not on
a Pi system, then it will not import the GPIO library and instead will
provide default test values.
"""

try:
  import RPi.GPIO as GPIO
  isRasPi = True
except:
  # Assume this is not running on a Raspberry Pi
  isRasPi = False

from constants import *

class BoardController:
  """
  Class for interacting with the Raspberry Pi GPIO pins
  """

  def __init__(self):
    """
    Initializes the Raspberry Pi board. It starts by
    setting all pins to input mode.
    """
    if isRasPi:
      GPIO.setmode(GPIO.BOARD)
      for pin in VALID_PINS:
        GPIO.setup(pin, GPIO.IN)
    self.pin_config = {
      pin: IN for pin in VALID_PINS
    }

  def __del__(self):
    """
    Destructor that cleans up any remaining GPIO configurations
    """
    if isRasPi:
      try:
        GPIO.cleanup()
      except:
        pass

  def set_pin_mode(self, pin, mode):
    """
    Changes the mode of a pin between input and output mode

    Parameters
    ----------
    pin: int
      The pin number as defined by the Raspberry Pi GPIO reference
    mode: int
      Number representing the mode: 0 for OUT, 1 for IN

    Returns
    -------
    int
      Pin mode: 0 for OUT, 1 for IN
    """
    if isRasPi:
      GPIO.setup(pin, mode)
    self.pin_config[pin] = mode
    return self.get_pin_mode(pin)

  def get_pin_mode(self, pin):
    """
    Gets the mode of the pin, either input or output

    Parameters
    ----------
    pin: int
      The pin number as defined by the Raspberry Pi GPIO reference

    Returns
    -------
    int
      Pin value: 0 for LOW, 1 for HIGH
    """
    return self.pin_config[pin]

  def set_pin_pwm(self, pin, duty, freq):
    raise NotImplementedError("'set_pin_pwm' method not implemented.")

  def get_pin_pwm(self, pin):
    raise NotImplementedError("'get_pin_pwm' method not implemented.")

  def get_pin_value(self, pin):
    """
    Gets the value of an input pin

    Parameters
    ----------
    pin: int
      The pin number as defined by the Raspberry Pi GPIO reference

    Returns
    -------
    int
      Pin value: 0 for LOW, 1 for HIGH
    """
    if isRasPi:
      return GPIO.input(pin)
    return 0 # mimics GPIO.LOW

  def set_pin_value(self, pin, value):
    """
    Sets the value of an output pin

    Parameters
    ----------
    pin: int
      The pin number as defined by the Raspberry Pi GPIO reference
    value: int
      Pin value: 0 for LOW, 1 for HIGH

    Returns
    -------
    int
      Pin value: 0 for LOW, 1 for HIGH
    """
    if isRasPi:
      GPIO.output(pin, value)
    return value
