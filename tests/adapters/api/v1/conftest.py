import pytest

from src.cross.enums import CartTypeEnum
from tests.factories import make_cart


@pytest.fixture
def create_reseller_cart_payload():
    return {"channel": "app", "cart_type": "reseller"}


@pytest.fixture
def create_customer_cart_payload():
    return {"channel": "portal", "cart_type": "customer"}


@pytest.fixture
def reseller_cart_api(fastapi_app):
    return make_cart(
        cart_type=CartTypeEnum.RESELLER, use_cases=fastapi_app.container
    )


@pytest.fixture
def customer_cart_api(fastapi_app):
    return make_cart(
        cart_type=CartTypeEnum.CUSTOMER, use_cases=fastapi_app.container
    )
