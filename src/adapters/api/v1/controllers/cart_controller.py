from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.adapters.api.global_exception_handler import GlobalExceptionHandler
from src.adapters.api.v1.dependencies.get_cart import get_cart_by_id
from src.adapters.api.v1.dependencies.services import (
    create_cart_service,
    factory_set_item_service,
    get_cart_service,
)
from src.adapters.api.v1.dto import AddItemDTO, CartResponseDTO, CreateCartDTO
from src.domain.entities.cart import Cart

router = APIRouter()


@router.post(
    "/v1/carts", status_code=HTTPStatus.CREATED, response_model=CartResponseDTO
)
async def create_cart(
    cart_in: CreateCartDTO,
):
    cart = create_cart_service.create(cart_in.to_cart())
    return CartResponseDTO.build_from_entity(cart)


@router.get(
    "/v1/carts/{cart_id}",
    status_code=HTTPStatus.OK,
    response_model=CartResponseDTO,
)
async def get_cart(
    cart_id: UUID,
):
    try:
        cart = get_cart_service.get(str(cart_id))
        return CartResponseDTO.build_from_entity(cart)
    except Exception as error:
        GlobalExceptionHandler.handler_get_cart_exceptions(error, cart_id)


@router.put(
    "/v1/carts/{cart_id}/items/{sku}",
    status_code=HTTPStatus.OK,
    response_model=CartResponseDTO,
)
async def add_new_item(
    cart_id: UUID,
    sku: str,
    add_item: AddItemDTO,
    cart: Cart = Depends(get_cart_by_id),
):

    try:
        set_item_service = factory_set_item_service(cart.cart_type)
        cart = set_item_service.set_item(
            cart=cart, sku=sku, quantity=add_item.quantity
        )
        return CartResponseDTO.build_from_entity(cart)
    except Exception as error:
        GlobalExceptionHandler.handler_set_item_exceptions(error, cart_id, sku)
