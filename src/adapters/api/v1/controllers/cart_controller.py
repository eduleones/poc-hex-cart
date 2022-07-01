from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.adapters.api.v1.dependencies.get_cart import get_cart_by_id
from src.adapters.api.v1.dependencies.services import (
    create_cart_service,
    factory_set_item_service,
    get_cart_service,
)
from src.adapters.api.v1.presentation import (
    AddItemPresenter,
    CartResponsePresenter,
    CreateCartPresenter,
)
from src.domain.entities.cart import Cart

router = APIRouter()


@router.post(
    "/v1/carts",
    status_code=HTTPStatus.CREATED,
    response_model=CartResponsePresenter,
)
async def create_cart(
    cart_in: CreateCartPresenter,
):
    cart = create_cart_service.create(cart_in.to_cart())
    return CartResponsePresenter.build_from_entity(cart)


@router.get(
    "/v1/carts/{cart_id}",
    status_code=HTTPStatus.OK,
    response_model=CartResponsePresenter,
)
async def get_cart(
    cart_id: UUID,
):
    cart = get_cart_service.get(str(cart_id))
    return CartResponsePresenter.build_from_entity(cart)


@router.put(
    "/v1/carts/{cart_id}/items/{sku}",
    status_code=HTTPStatus.OK,
    response_model=CartResponsePresenter,
)
async def add_new_item(
    cart_id: UUID,
    sku: str,
    add_item: AddItemPresenter,
    cart: Cart = Depends(get_cart_by_id),
):

    set_item_service = factory_set_item_service(cart.cart_type)
    cart = set_item_service.set_item(
        cart=cart, sku=sku, quantity=add_item.quantity
    )
    return CartResponsePresenter.build_from_entity(cart)
