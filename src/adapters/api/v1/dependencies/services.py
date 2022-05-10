from src.cross.containers import ServicesContainer
from src.cross.enums import CartTypeEnum

create_cart_service = ServicesContainer.create_cart_service()
get_cart_service = ServicesContainer.get_cart_service()


def factory_set_item_service(cart_type: CartTypeEnum):
    if cart_type == CartTypeEnum.RESELLER:
        return ServicesContainer.reseller_set_item_service()
    return ServicesContainer.customer_set_item_service()
