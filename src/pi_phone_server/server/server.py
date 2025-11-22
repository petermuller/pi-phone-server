from flask import Flask, jsonify
from flask_cors import CORS

from pi_phone_server.exception.exceptions import InvalidOperationError, InvalidPinError
from pi_phone_server.server.pin_operations.pin_operations import pin_bp


app = Flask(__name__)
CORS(app)
app.register_blueprint(pin_bp, url_prefix="/v1")


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.errorhandler(InvalidOperationError)
def handle_invalid_operation(exc):
    """
    Error raised because the user tried to write to an input pin.
    """
    return jsonify({"error": str(exc)}), 400


@app.errorhandler(InvalidPinError)
def handle_invalid_pin(exc):
    """
    Error raised because the user specified a pin that does not exist.
    """
    return jsonify({"error": str(exc)}), 400
