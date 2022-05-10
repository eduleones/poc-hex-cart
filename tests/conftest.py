import pytest
from httpx import AsyncClient

from src.adapters.api.main import app
from src.cross.containers import (
    ExternalResourcesContainer,
    RepositoryContainer,
)
from src.cross.enums import CartTypeEnum
from tests.factories import make_cart


@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(
        app=app, base_url="http://localhost", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture
def cart_repository_service():
    return RepositoryContainer.mock_cart_repository()


@pytest.fixture
def reseller_inventory_resource():
    return ExternalResourcesContainer.reseller_inventory_resource()


@pytest.fixture
def customer_inventory_resource():
    return ExternalResourcesContainer.customer_inventory_resource()


@pytest.fixture
def product_resource():
    return ExternalResourcesContainer.product_resource()


@pytest.fixture
def reseller_cart():
    return make_cart(cart_type=CartTypeEnum.RESELLER)


@pytest.fixture
def customer_cart():
    return make_cart(cart_type=CartTypeEnum.CUSTOMER)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
