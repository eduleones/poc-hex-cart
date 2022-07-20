from http import HTTPStatus
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.adapters.api.containers import UseCases
from src.adapters.api.v1.presentation import (
    AddItemPresenter,
    CartResponsePresenter,
    CreateCartPresenter,
)
from src.cross.enums import CartTypeEnum
from src.domain.entities import Cart
from src.domain.ports.input.set_item import SetItemInterface

router = APIRouter()


@router.post(
    "/v1/carts",
    status_code=HTTPStatus.CREATED,
    response_model=CartResponsePresenter,
)
@inject
async def create_cart(
    cart_in: CreateCartPresenter,
    use_case=Depends(Provide[UseCases.create_cart]),
):
    cart = use_case.create(cart_in.to_cart())
    return CartResponsePresenter.build_from_entity(cart)


@router.get(
    "/v1/carts/{cart_id}",
    status_code=HTTPStatus.OK,
    response_model=CartResponsePresenter,
)
@inject
async def get_cart(
    cart_id: UUID,
    use_case=Depends(Provide[UseCases.get_cart]),
):
    cart = use_case.get(str(cart_id))
    return CartResponsePresenter.build_from_entity(cart)


@inject
def _get_cart(
    cart_id: UUID, use_case=Depends(Provide[UseCases.get_cart])
) -> Cart:
    a = use_case.get(cart_id=str(cart_id))
    return a


def _get_set_item_use_case(cart: Cart):
    breakpoint()
    if cart.cart_type == CartTypeEnum.CUSTOMER:
        return UseCases.customer_set_item()
    else:
        return UseCases.reseller_set_item()


@router.put(
    "/v1/carts/{cart_id}/items/{sku}",
    status_code=HTTPStatus.OK,
    response_model=CartResponsePresenter,
)
@inject
async def add_new_item(
    cart_id: UUID,
    sku: str,
    add_item: AddItemPresenter,
    cart: Cart = Depends(_get_cart),
    use_case: SetItemInterface = Depends(_get_set_item_use_case),
):
    cart = use_case.set_item(cart=cart, sku=sku, quantity=add_item.quantity)
    return CartResponsePresenter.build_from_entity(cart)
