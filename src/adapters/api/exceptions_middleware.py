from http import HTTPStatus
from typing import Dict, Type

from fastapi import Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.base import DomainException
from src.domain.exceptions.cart_exception import CartNotFoundException
from src.domain.exceptions.inventory_expection import (
    InventoryNotFoundException,
)
from src.domain.exceptions.product_exception import ProductNotFoundException

_map: Dict[Type[DomainException], JSONResponse] = {
    CartNotFoundException: JSONResponse(
        "This cart doesnt exist", status_code=HTTPStatus.NOT_FOUND
    ),
    InventoryNotFoundException: JSONResponse(
        "There is not enough in inventory", status_code=HTTPStatus.BAD_REQUEST
    ),
    ProductNotFoundException: JSONResponse(
        "Item not found on Products API", status_code=HTTPStatus.NOT_FOUND
    ),
}
default_response = JSONResponse(
    "Internal server error", status_code=HTTPStatus.INTERNAL_SERVER_ERROR
)


async def catch_exceptions_middleware(
    request: Request, call_next
) -> JSONResponse:
    try:
        return await call_next(request)
    except DomainException as e:
        response = _map.get(e.__class__, default_response)
        return response

    except Exception as e:
        return default_response
