from enum import Enum


class ChannelEnum(str, Enum):
    APP = "app"
    PORTAL = "portal"


class CartStatusEnum(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


class CartTypeEnum(str, Enum):
    CUSTOMER = "customer"
    RESELLER = "reseller"


class CartErrorEnum(str, Enum):
    CART_GENERIC_ERROR = "cart_generic_error"
    CART_NOT_FOUND = "cart_not_found"
    CART_ALREADY_CLOSED = "cart_already_closed"
    CART_ALREADY_OPEN = "cart_already_open"
    CART_ITEM_NOT_FOUND = "cart_item_not_found"
    CART_ITEM_OUT_OF_STOCK = "cart_item_out_of_stock"
    CART_ITEM_INVALID_INVENTORY = "cart_item_invalid_inventory"
    CART_ITEM_QUANTITY_INVALID = "cart_item_quantity_invalid"
    CART_ITEM_QUANTITY_ZERO = "cart_item_quantity_zero"
    CART_ITEM_QUANTITY_MAX = "cart_item_quantity_max"
    CART_ITEM_PRICE_INVALID = "cart_item_price_invalid"
    CART_ITEM_PRICE_ZERO = "cart_item_price_zero"
    CART_ITEM_PRICE_MAX = "cart_item_price_max"
    CART_ITEM_PRICE_MIN = "cart_item_price_min"
    CART_ITEM_PRICE_TOTAL_MAX = "cart_item_price_total_max"
    CART_ITEM_PRICE_TOTAL_MIN = "cart_item_price_total_min"
    CART_ITEM_PRICE_TOTAL_ZERO = "cart_item_price_total_zero"
    CART_ITEM_PRICE_TOTAL_INVALID = "cart_item_price_total_invalid"
