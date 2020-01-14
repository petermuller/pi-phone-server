#!/usr/bin/env python3
"""
PiServer.py

Listens for incoming connections and orchestrates the server commands.
"""

from flask import Flask
from BoardController import BoardController
from constants import *

app = Flask(__name__)
bc = BoardController()

def validate_pin(pin):
  if pin not in VALID_PINS:
    raise ValueError(f"Pin {pin} is not in the list of valid pins: {VALID_PINS}")

@app.route("/")
def hello_world():
  return "Server is on"

@app.route("/set-pin-mode/<int:pin>/<string:mode>")
def set_pin_mode(pin, mode):
  """
  Sets GPIO pin as either an input or output pin.
  An input pin is one that detects logical high or low values.
  An output pin is one that produces a variable average voltage with
    pulse width modulation (PWM).

  Parameters
  ----------
  pin: int
    The pin number as defined by the Raspberry Pi GPIO reference
  mode: str
    The pin mode. Can be either 'input' or 'output'

  Returns
  -------
  dict
  """
  validate_pin(pin)
  if mode not in VALID_MODES:
    raise ValueError(f"Mode {mode} not in valid modes: {VALID_MODES}")
  pin_mode = bc.set_pin_mode(pin, MODE_MAP[mode])
  return {
    'pin': pin,
    'mode': pin_mode
  }

@app.route("/get-pin-mode/<int:pin>")
def get_pin_mode(pin):
  """
  Gets the GPIO pin configuration for the specified pin

  Parameters
  ----------
  pin: int
    The pin number as defined by the Raspberry Pi GPIO reference

  Returns
  -------
  dict
  """
  validate_pin(pin)
  mode = bc.get_pin_mode(pin)
  return {
    'pin': pin,
    'mode': mode
  }

@app.route("/set-pin-pwm/<int:pin>/<float:duty>")
@app.route("/set-pin-pwm/<int:pin>/<float:duty>/<float:freq>")
def set_pin_pwm(pin, duty, freq=100):
  """
  Sets the PWM config for an output pin

  Parameters
  ----------
  pin: int
    The pin number as defined by the Raspberry Pi GPIO reference
  duty: float
    The duty cycle of the PWM. Must be value constrained to 0.0 <= n <= 100.0
  freq: float, optional
    The PWM frequency, in Hertz. Must be value greater than 0.0.

  Returns
  -------
  dict
  """
  validate_pin(pin)
  duty, freq = bc.set_pin_pwm(pin, duty, freq)
  return {
    'pin': pin,
    'duty': duty,
    'freq': freq
  }

@app.route("/get-pin-pwm/<int:pin>")
def get_pin_pwm(pin):
  """
  Gets the PWM config for an output pin

  Parameters
  ----------
  pin: int
    The pin number as defined by the Raspberry Pi GPIO reference

  Returns
  -------
  dict
  """
  validate_pin(pin)
  duty, freq = bc.get_pin_pwm(pin)
  return {
    'pin': pin,
    'duty': duty,
    'freq': freq
  }

@app.route("/set-pin-value/<int:pin>/<int:value>")
def set_pin_value(pin, value):
  """
  Sets the value, either "HIGH" or "LOW," for an output pin.

  Parameters
  ----------
  pin: int
    The pin number as defined by the Raspberry Pi GPIO reference
  value: int
    The HIGH or LOW value to set the pin

  Returns
  -------
  dict
  """
  validate_pin(pin)
  if not bc.get_pin_mode(pin) == OUT:
    raise RuntimeError(f"Pin {pin} is not in OUT mode")
  if not value in VALID_VOLTAGES:
    raise ValueError(f"Value {value} not in valid voltages: {VALID_VOLTAGES}")
  return {
    'pin': pin,
    'value': bc.set_pin_value(pin, value)
  }

@app.route("/get-pin-value/<int:pin>")
def get_pin_value(pin):
  """
  Gets the value, either "HIGH" or "LOW," for an input pin.

  Parameters
  ----------
  pin: int
    The pin number as defined by the Raspberry Pi GPIO reference

  Returns
  -------
  dict
  """
  validate_pin(pin)
  if not bc.get_pin_mode(pin) == IN:
    raise RuntimeError(f"Pin {pin} is not in IN mode")
  return {
    'pin': pin,
    'value': bc.get_pin_value(pin)
  }

@app.errorhandler(NotImplementedError)
def handle_not_implemented_error(e):
  return {
      "Error": "Method not implemented",
      "Message": str(e)
    }, 501

@app.errorhandler(ValueError)
def handle_value_error(e):
  return {
      "Error": "Value failed validation",
      "Message": str(e)
    }, 400

@app.errorhandler(RuntimeError)
def handle_value_error(e):
  return {
      "Error": "Method and pin mode do not match",
      "Message": str(e)
    }, 400

# Run the server. Flask will default to port 5000.
if __name__ == "__main__":
  app.run(debug = True,
          host = "0.0.0.0")
