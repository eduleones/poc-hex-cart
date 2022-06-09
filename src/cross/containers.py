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
from src.domain.use_cases import (
    CreateCartService,
    CustomerSetItemService,
    GetCartService,
    ResellerSetItemService,
)


class RepositoryContainer(containers.DeclarativeContainer):
    cart_respository: CartRepositoryInterface = providers.Singleton(
        RedisCartRepository
    ).add_args(1)

    mock_cart_repository: CartRepositoryInterface = providers.Singleton(
        MockRedisCartRepository
    ).add_args(1)


class ExternalResourcesContainer(containers.DeclarativeContainer):
    reseller_inventory_resource: InventoryResourceInterface = (
        providers.Factory(MockResellerStockApi)
    )
    customer_inventory_resource: InventoryResourceInterface = (
        providers.Factory(MockCustomerStockApi)
    )
    product_resource: ProductResourceInterface = providers.Factory(
        MockProductApi
    )


class ServicesContainer(containers.DeclarativeContainer):
    # Create Cart Service
    create_cart_service: CreateCartInterface = providers.Factory(
        CreateCartService,
        cart_repository=RepositoryContainer.mock_cart_repository,
    )
    mock_create_cart_service: CreateCartInterface = providers.Factory(
        CreateCartService,
        cart_repository=RepositoryContainer.mock_cart_repository,
    )

    # Get Cart Service
    get_cart_service: GetCartInterface = providers.Factory(
        GetCartService,
        cart_repository=RepositoryContainer.mock_cart_repository,
    )

    # Set Item Service
    reseller_set_item_service: SetItemInterface = providers.Factory(
        ResellerSetItemService,
        cart_repository=RepositoryContainer.mock_cart_repository,
        inventory_resource=(
            ExternalResourcesContainer.reseller_inventory_resource
        ),
        product_resource=ExternalResourcesContainer.product_resource,
    )

    customer_set_item_service: SetItemInterface = providers.Factory(
        CustomerSetItemService,
        cart_repository=RepositoryContainer.mock_cart_repository,
        inventory_resource=(
            ExternalResourcesContainer.customer_inventory_resource
        ),
        product_resource=ExternalResourcesContainer.product_resource,
    )
