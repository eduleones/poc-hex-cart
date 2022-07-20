from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from src.cross.enums import CartErrorEnum
from src.cross.error_map import ErrorMap

Dto = TypeVar("Dto", bound=BaseModel)


class BaseError(BaseModel):
    error_code: CartErrorEnum
    message: str

    def raise_error(self):
        raise ErrorMap[self.error_code]


@dataclass
class Result(Generic[Dto]):
    error: Optional[BaseError] = None
    data: Optional[Dto] = None

    @property
    def is_success(self) -> bool:
        return bool(self.data) and not self.error
