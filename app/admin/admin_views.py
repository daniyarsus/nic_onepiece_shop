from app.admin.models.user import UserAdmin
from app.admin.models.product import ProductAdmin
from app.admin.models.payment import PaymentAdmin


all_views = [
    UserAdmin,
    ProductAdmin,
    PaymentAdmin
]
