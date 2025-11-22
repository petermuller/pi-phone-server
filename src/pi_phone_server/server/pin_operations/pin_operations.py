import platform

from flask import Blueprint, request, jsonify
from pi_phone_server.model.api.datatypes import *
from pi_phone_server.model.controller.board import Board
from pi_phone_server.model.controller.pin import PinMode, Voltage


pin_bp = Blueprint("pins", __name__)
board = Board(is_pi=platform.machine().startswith("arm"))


def _mode_to_int(mode: PinMode) -> int:
    return int(mode)


def _voltage_to_int(voltage: Voltage) -> int:
    return int(voltage)


@pin_bp.get("/<int:pin_id>")
def get_pin_info(pin_id: int):
    summary = board.pin(pin_id).get_summary()
    return jsonify({
        "pin_id": pin_id,
        "mode": _mode_to_int(summary.mode),
        "voltage": _voltage_to_int(summary.voltage)
    }), 200


@pin_bp.get("/<int:pin_id>/mode")
def get_pin_mode(pin_id: int):
    pin = board.pin(pin_id)
    return jsonify({
        "pin_id": pin_id,
        "mode": _mode_to_int(pin.mode)
    }), 200


@pin_bp.post("/<int:pin_id>/mode")
def set_pin_mode(pin_id: int):
    data = request.get_json()
    if not data or "mode" not in data:
        return jsonify({"error": "mode is required"}), 400

    try:
        mode = PinMode(data["mode"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid mode"}), 400

    pin = board.pin(pin_id)
    pin.mode = mode
    return jsonify({
        "pin_id": pin_id,
        "mode": _mode_to_int(pin.mode)
    }), 200


@pin_bp.get("/<int:pin_id>/voltage")
def get_pin_voltage(pin_id: int):
    pin = board.pin(pin_id)
    return jsonify({
        "pin_id": pin_id,
        "voltage": _voltage_to_int(pin.voltage)
    }), 200


@pin_bp.post("/<int:pin_id>/voltage")
def set_pin_voltage(pin_id: int):
    data = request.get_json()
    if not data or "voltage" not in data:
        return jsonify({"error": "voltage is required"}), 400

    try:
        voltage = Voltage(data["voltage"])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid voltage"}), 400

    pin = board.pin(pin_id)
    pin.voltage = voltage
    return jsonify({
        "pin_id": pin_id,
        "voltage": _voltage_to_int(pin.voltage)
    }), 200
