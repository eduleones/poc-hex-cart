from fastapi import FastAPI

from src.adapters.api.v1.controllers.cart_controller import (
    router as cart_router,
)
from src.cross.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
    )
    application.include_router(cart_router)

    return application


app = get_application()
