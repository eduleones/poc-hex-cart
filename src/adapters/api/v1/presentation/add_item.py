from pydantic import BaseModel


class AddItemPresenter(BaseModel):
    quantity: int
