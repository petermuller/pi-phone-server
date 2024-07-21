from fastapi.responses import JSONResponse


class InvalidInputError(JSONResponse):

    def __init__(self, exc: Exception):
        super().__init__(
            status_code=400,
            content={
                "error": str(exc)
            }
        )
