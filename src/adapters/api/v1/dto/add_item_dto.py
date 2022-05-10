from pydantic import BaseModel


class AddItemDTO(BaseModel):
    quantity: int
