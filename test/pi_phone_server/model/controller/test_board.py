import platform
import pytest

from pi_phone_server.exception.exceptions import InvalidPinError
from pi_phone_server.model.controller.board import Board, VALID_PINS
from pi_phone_server.model.controller.pin import Pin


class TestBoard:

    @staticmethod
    def get_board(is_pi: bool):
        return Board(is_pi)

    def test_valid_pins(self):
        board = self.get_board(False)
        for pin_id in range(24):
            if pin_id in VALID_PINS:
                pin = board.pin(pin_id=pin_id)
                assert isinstance(pin, Pin)
            else:
                with pytest.raises(InvalidPinError):
                    board.pin(pin_id=pin_id)
                    pytest.fail(f"Expected pin {pin_id} to be invalid")

    def test_valid_pins_pi(self):
        if platform.machine().startswith("arm"):
            board = self.get_board(True)
            assert isinstance(board, Board)
        else:
            with pytest.raises(ModuleNotFoundError):
                self.get_board(True)
