import platform

from fastapi import APIRouter
from pi_phone_server.model.api.datatypes import *
from pi_phone_server.model.controller.board import Board


pin_router = APIRouter()
board = Board(is_pi=platform.machine().startswith("arm"))


@pin_router.get("/{pin_id}")
async def get_pin_info(pin_id: int) -> PinSummaryResponse:
    summary = board.pin(pin_id).get_summary()
    return PinSummaryResponse(
        pin_id=pin_id,
        mode=summary.mode,
        voltage=summary.voltage
    )


@pin_router.get("/{pin_id}/mode")
async def get_pin_mode(pin_id: int) -> PinModeResponse:
    return PinModeResponse(
        pin_id=pin_id,
        mode=board.pin(pin_id).mode
    )


@pin_router.post("/{pin_id}/mode")
async def set_pin_mode(pin_id: int, request: SetPinModeRequest) -> PinModeResponse:
    board.pin(pin_id).mode = request.mode
    return PinModeResponse(
        pin_id=pin_id,
        mode=board.pin(pin_id).mode
    )


@pin_router.get("/{pin_id}/voltage")
async def get_pin_voltage(pin_id: int) -> PinVoltageResponse:
    return PinVoltageResponse(
        pin_id=pin_id,
        voltage=board.pin(pin_id).voltage
    )


@pin_router.post("/{pin_id}/voltage")
async def set_pin_voltage(pin_id: int, request: SetPinVoltageRequest) -> PinVoltageResponse:
    board.pin(pin_id).voltage = request.voltage
    return PinVoltageResponse(
        pin_id=pin_id,
        voltage=board.pin(pin_id).voltage
    )
