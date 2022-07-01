from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from src.cross.enums import CartErrorEnum, ErrorMap

Dto = TypeVar("Dto", bound=BaseModel)


class BaseError(BaseModel):
    error_code: CartErrorEnum
    message: str

    def raise_error(self):
        raise ErrorMap[self.error_code]


class Result(BaseModel, Generic[Dto]):
    error = Optional[BaseError]
    data: Optional[Dto]

    @property
    def is_success(self) -> bool:
        return bool(self.data) and not self.error

    class Config:
        arbitrary_types_allowed = True


# Num arquivo ports especifico
class SkuDto(BaseModel):
    quantity: int
    price: float


class WrongDto(BaseModel):
    a: int


def adapter() -> Result[SkuDto]:
    return Result[SkuDto](error=None, data=SkuDto(quantity=1, price=2.0))


def use_case(result: Result[SkuDto]):
    if result.data:
        a = result.data
        a
