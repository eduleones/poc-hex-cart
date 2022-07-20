from fastapi import FastAPI

from src.adapters.api.containers import UseCases, get_adapter
from src.adapters.api.v1.controllers.cart_controller import (
    router as cart_router,
)
from src.settings import settings

from .exceptions_middleware import catch_exceptions_middleware


def get_application() -> FastAPI:
    container = UseCases(adapters=get_adapter())
    container.wire(modules=["src.adapters.api.v1.controllers.cart_controller"])

    application = FastAPI(
        title=settings.PROJECT_NAME,
    )
    application.container = container  # type: ignore
    application.include_router(cart_router)
    application.middleware("http")(catch_exceptions_middleware)

    return application


app = get_application()
