from app.repository.user import UserRepository

from app.service.register import RegisterService
from app.service.login import LoginService
from app.service.password import PasswordService
from app.service.logout import LogoutService

from app.service.balance import BalanceService


from app.repository.product import ProductRepository

from app.service.product import ProductService


from app.repository.payment import PaymentRepository

from app.service.payment import PaymentService


def register_service():
    return RegisterService(UserRepository)


def login_service():
    return LoginService(UserRepository)


def password_service():
    return PasswordService(UserRepository)


def logout_service():
    return LogoutService


def product_service():
    return ProductService(ProductRepository)


def payment_service():
    return PaymentService(PaymentRepository)


def balance_service():
    return BalanceService(UserRepository)
