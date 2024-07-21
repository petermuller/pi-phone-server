from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pi_phone_server.exception.exceptions import InvalidOperationError, InvalidPinError
from pi_phone_server.model.api.errors import InvalidInputError
from pi_phone_server.server.pin_operations.pin_operations import pin_router


app = FastAPI()
app.include_router(pin_router, prefix="/v1")


@app.get("/health")
async def health():
    return JSONResponse(
        content={"status": "ok"},
        status_code=200,
    )


@app.exception_handler(InvalidOperationError)
async def handle_invalid_operation(request: Request, exc: InvalidOperationError) -> InvalidInputError:
    """
    Error raised because the user tried to write to an input pin.
    """
    return InvalidInputError(exc)


@app.exception_handler(InvalidPinError)
async def handle_invalid_pin(request: Request, exc: InvalidPinError) -> InvalidInputError:
    """
    Error raised because the user specified a pin that does not exist.
    """
    return InvalidInputError(exc)
