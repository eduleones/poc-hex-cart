import pytest

from src.adapters.api.v1.presentation.create_cart import CreateCartPresenter
from src.cross.enums import CartTypeEnum, ChannelEnum
from src.domain.ports.input.create_cart import CreateCartInterface
from src.domain.ports.input.get_cart import GetCartInterface
from src.domain.ports.input.set_item import SetItemInterface
from tests.factories import make_cart


@pytest.fixture
def create_cart_use_case(use_cases) -> CreateCartInterface:
    return use_cases.create_cart()


@pytest.fixture
def get_cart_use_case(use_cases) -> GetCartInterface:
    return use_cases.get_cart()


@pytest.fixture
def reseller_set_item_use_case(use_cases) -> SetItemInterface:
    return use_cases.reseller_set_item()


@pytest.fixture
def customer_set_item_use_case(use_cases) -> SetItemInterface:
    return use_cases.customer_set_item()


@pytest.fixture
def create_reseller_cart_presenter():
    return CreateCartPresenter(
        channel=ChannelEnum.APP, cart_type=CartTypeEnum.RESELLER
    )


@pytest.fixture
def create_customer_cart_presenter():
    return CreateCartPresenter(
        channel=ChannelEnum.APP, cart_type=CartTypeEnum.CUSTOMER
    )
