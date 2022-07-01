from typing import Dict, Type

from fastapi import Request
from fastapi.responses import JSONResponse

_map_from_domain_to_http: Dict[Type[Exception], JSONResponse] = {}


async def catch_exceptions_middleware(
    request: Request, call_next
) -> JSONResponse:
    try:
        return await call_next(request)
    except Exception as e:
        default_response = JSONResponse(
            "Internal server error", status_code=500
        )
        response = _map_from_domain_to_http.get(e.__class__, default_response)
        return response
