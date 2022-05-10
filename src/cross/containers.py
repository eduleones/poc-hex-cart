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
    ICreateCartService,
    IGetCartService,
    ISetItemService,
)
from src.domain.ports.output import (
    ICartRepository,
    IInventoryResource,
    IProductResource,
)
from src.domain.services import (
    CreateCartService,
    CustomerSetItemService,
    GetCartService,
    ResellerSetItemService,
)


class RepositoryContainer(containers.DeclarativeContainer):
    cart_respository: ICartRepository = providers.Singleton(
        RedisCartRepository
    ).add_args(1)

    mock_cart_repository: ICartRepository = providers.Singleton(
        MockRedisCartRepository
    ).add_args(1)


class ExternalResourcesContainer(containers.DeclarativeContainer):
    reseller_inventory_resource: IInventoryResource = providers.Factory(
        MockResellerStockApi
    )
    customer_inventory_resource: IInventoryResource = providers.Factory(
        MockCustomerStockApi
    )
    product_resource: IProductResource = providers.Factory(MockProductApi)


class ServicesContainer(containers.DeclarativeContainer):
    # Create Cart Service
    create_cart_service: ICreateCartService = providers.Factory(
        CreateCartService,
        cart_repository=RepositoryContainer.mock_cart_repository,
    )
    mock_create_cart_service: ICreateCartService = providers.Factory(
        CreateCartService,
        cart_repository=RepositoryContainer.mock_cart_repository,
    )

    # Get Cart Service
    get_cart_service: IGetCartService = providers.Factory(
        GetCartService,
        cart_repository=RepositoryContainer.mock_cart_repository,
    )

    # Set Item Service
    reseller_set_item_service: ISetItemService = providers.Factory(
        ResellerSetItemService,
        cart_repository=RepositoryContainer.mock_cart_repository,
        inventory_resource=(
            ExternalResourcesContainer.reseller_inventory_resource
        ),
        product_resource=ExternalResourcesContainer.product_resource,
    )

    customer_set_item_service: ISetItemService = providers.Factory(
        CustomerSetItemService,
        cart_repository=RepositoryContainer.mock_cart_repository,
        inventory_resource=(
            ExternalResourcesContainer.customer_inventory_resource
        ),
        product_resource=ExternalResourcesContainer.product_resource,
    )
