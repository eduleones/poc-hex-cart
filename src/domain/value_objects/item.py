from pydantic import BaseModel


class Item(BaseModel):
    sku: str
    name: str
    description: str
    quantity: int
    price: float
