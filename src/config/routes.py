from fastapi import FastAPI

from src.modules.users import routes as user_router
from src.modules.two_factor import routes as two_factor_router
from src.modules.number_lucky import routes as number_lucky_router
from src.modules.guests import routes as guest_router

def init_app(app: FastAPI) -> None:
    app.include_router(user_router.router)
    app.include_router(two_factor_router.router)
    app.include_router(number_lucky_router.router)
    app.include_router(guest_router.router)
    