#!/usr/bin/env python3
"""
Constants for use in parameter validation for the server
"""

LOW = 0 # compatible with GPIO.LOW
HIGH = 1 # compatible with GPIO.HIGH
OUT = 0 # compatible with GPIO.OUT
IN = 1 # compatible with GPIO.IN

VALID_MODES = ["IN", "OUT"]
VALID_PINS = [7, 11, 12, 13, 15, 16, 18, 22]
VALID_VOLTAGES = [LOW, HIGH]

VOLTAGE_MAP = {
  "LOW": LOW,
  LOW: "LOW",
  "HIGH": HIGH,
  HIGH: "HIGH"
}

MODE_MAP = {
  "OUT": OUT,
  OUT: "OUT",
  "IN": IN,
  IN: "IN"
}
