import pytest
from httpx import AsyncClient

from src.adapters.api.containers import TestAdapters, UseCases, get_adapter
from src.adapters.api.main import app
from src.cross.enums import CartTypeEnum
from tests.factories import make_cart


@pytest.fixture
def adapters():
    return TestAdapters()


@pytest.fixture
def use_cases():
    container = UseCases(adapters=get_adapter())
    return container


@pytest.fixture(scope="module")
def fastapi_app():
    return app


@pytest.fixture(scope="module")
async def async_client(fastapi_app):
    async with AsyncClient(
        app=fastapi_app, base_url="http://localhost", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture
def cart_repository(adapters):
    return adapters.cart_repository()


@pytest.fixture
def reseller_inventory_resource(adapters):
    return adapters.reseller_inventory_resource()


@pytest.fixture
def customer_inventory_resource(adapters):
    return adapters.customer_inventory_resource()


@pytest.fixture
def product_resource(adapters):
    return adapters.product_resource()


@pytest.fixture
def reseller_cart(use_cases):
    return make_cart(cart_type=CartTypeEnum.RESELLER, use_cases=use_cases)


@pytest.fixture
def customer_cart():
    return make_cart(cart_type=CartTypeEnum.CUSTOMER)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
