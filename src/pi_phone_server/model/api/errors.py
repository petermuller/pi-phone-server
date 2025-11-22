from dataclasses import dataclass


@dataclass
class InvalidInputError:
    error: str

    def __init__(self, exc: Exception):
        self.error = str(exc)
