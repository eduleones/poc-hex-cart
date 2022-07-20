from sqlite3 import adapters
from typing import Optional

from pytest import fixture

from src.adapters.api.containers import TestAdapters, UseCases, get_adapter
from src.adapters.api.v1.presentation.create_cart import CreateCartPresenter
from src.cross.enums import CartTypeEnum, ChannelEnum
from src.domain.entities import Cart


def make_cart(
    channel: ChannelEnum = ChannelEnum.APP,
    cart_type: CartTypeEnum = CartTypeEnum.RESELLER,
    use_cases=None,
) -> Cart:
    cart_dto = CreateCartPresenter(channel=channel, cart_type=cart_type)
    if use_cases is None:
        use_cases = UseCases(adapters=TestAdapters())

    return use_cases.create_cart().create(cart_dto.to_cart())
