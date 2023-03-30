import sentry_sdk
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

#from src.auth.router import router as auth_router
#from src.config import app_configs, settings
#from src.database import database

sentry_sdk.init(
    dsn="https://f4a878fe81244afab3c3a6ac55bc204d@o4504916438351872.ingest.sentry.io/4504916441366528",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

# app = FastAPI(**app_configs)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.CORS_ORIGINS,
#     allow_origin_regex=settings.CORS_ORIGINS_REGEX,
#     allow_credentials=True,
#     allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
#     allow_headers=settings.CORS_HEADERS,
# )

# if settings.ENVIRONMENT.is_deployed:
#     sentry_sdk.init(
#         dsn=settings.SENTRY_DSN,
#         environment=settings.ENVIRONMENT,
#         traces_sample_rate=1.0,
#     )


# @app.on_event("startup")
# async def startup() -> None:
#     pool = aioredis.ConnectionPool.from_url(
#         settings.REDIS_URL, max_connections=10, decode_responses=True
#     )
#     redis.redis_client = aioredis.Redis(connection_pool=pool)
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown() -> None:
#     await database.disconnect()
#     await redis.redis_client.close()


# @app.get("/healthcheck", include_in_schema=False)
# async def healthcheck() -> dict[str, str]:
#     return {"status": "ok"}


# app.include_router(auth_router, prefix="/auth", tags=["Auth"])

app = FastAPI()

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0