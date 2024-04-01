from app.api.client.auth import router as auth_router
from app.api.client.shop import router as shop_router
from app.api.client.payment import router as payment_router
from app.api.client.balance import router as balance_router


all_routers = [
    auth_router,
    shop_router,
    payment_router,
    balance_router
]
