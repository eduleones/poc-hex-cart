from dependency_injector import containers, providers

from src.adapters.db.mock import MockRedisCartRepository
from src.adapters.db.redis import RedisCartRepository
from src.adapters.external_resources.inventory.mock_customer_stock_api import (
    MockCustomerStockApi,
)
from src.adapters.external_resources.inventory.mock_reseller_stock_api import (
    MockResellerStockApi,
)
from src.adapters.external_resources.product.mock_product_api import (
    MockProductApi,
)
from src.domain.ports.input import (
    CreateCartInterface,
    GetCartInterface,
    SetItemInterface,
)
from src.domain.ports.output import (
    CartRepositoryInterface,
    InventoryResourceInterface,
    ProductResourceInterface,
)
from src.domain.use_cases.create_cart import CreateCartUseCase
from src.domain.use_cases.get_cart import GetCartUseCase
from src.domain.use_cases.set_item.customer import CustomerSetItemUseCase
from src.domain.use_cases.set_item.reseller import ResellerSetItemUseCase


class TestAdapters(containers.DeclarativeContainer):
    cart_repository: CartRepositoryInterface = providers.Singleton(
        MockRedisCartRepository
    ).add_args(1)
    reseller_inventory_resource: InventoryResourceInterface = (
        providers.Factory(MockResellerStockApi)
    )
    customer_inventory_resource: InventoryResourceInterface = (
        providers.Factory(MockCustomerStockApi)
    )
    product_resource: ProductResourceInterface = providers.Factory(
        MockProductApi
    )


class Adapters(containers.DeclarativeContainer):
    cart_repository: CartRepositoryInterface = providers.Singleton(
        RedisCartRepository
    ).add_args(1)
    reseller_inventory_resource: InventoryResourceInterface = (
        providers.Factory(MockResellerStockApi)
    )
    customer_inventory_resource: InventoryResourceInterface = (
        providers.Factory(MockCustomerStockApi)
    )
    product_resource: ProductResourceInterface = providers.Factory(
        MockProductApi
    )


class UseCases(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    create_cart: CreateCartInterface = providers.Factory(
        CreateCartUseCase, cart_repository=adapters.cart_repository
    )
    get_cart: GetCartInterface = providers.Factory(
        GetCartUseCase,
        cart_repository=adapters.cart_repository,
    )
    reseller_set_item: SetItemInterface = providers.Factory(
        ResellerSetItemUseCase,
        cart_repository=adapters.cart_repository,
        inventory_resource=adapters.reseller_inventory_resource,
        product_resource=adapters.product_resource,
    )
    customer_set_item: SetItemInterface = providers.Factory(
        CustomerSetItemUseCase,
        cart_repository=adapters.cart_repository,
        inventory_resource=adapters.customer_inventory_resource,
        product_resource=adapters.product_resource,
    )


def get_adapter():
    import os

    if os.getenv("ENVIRONMENT") == "TEST":
        return TestAdapters()
    return Adapters()
