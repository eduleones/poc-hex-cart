import pytest

from src.adapters.api.v1.presentation.create_cart import CreateCartDTO
from src.cross.enums import CartTypeEnum, ChannelEnum


@pytest.fixture
def create_reseller_cart_dto():
    return CreateCartDTO(
        channel=ChannelEnum.APP, cart_type=CartTypeEnum.RESELLER
    )


@pytest.fixture
def create_customer_cart_dto():
    return CreateCartDTO(
        channel=ChannelEnum.APP, cart_type=CartTypeEnum.CUSTOMER
    )
