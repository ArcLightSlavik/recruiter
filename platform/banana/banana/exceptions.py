from fastapi.requests import Request
from fastapi.responses import JSONResponse


class CredentialsException(Exception):
    pass


def credentials_exception_handler(_request: Request, _exc: CredentialsException):
    return JSONResponse(
        status_code=401,
        content=dict(message="Could not validate credentials"),
        headers={"WWW-Authenticate": "Bearer"},
    )
