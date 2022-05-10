import pytest


@pytest.fixture
def create_reseller_cart_payload():
    return {"channel": "app", "cart_type": "reseller"}


@pytest.fixture
def create_customer_cart_payload():
    return {"channel": "portal", "cart_type": "customer"}
