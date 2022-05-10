from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    PROJECT_NAME: str = "Cart API"

    # Database
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    CART_TTL = 60 * 60 * 24 * 7  # 7 days


settings = BaseSettings()
