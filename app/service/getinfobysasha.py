from fastapi import HTTPException
from app.settings.db.connection import sync_DB_URL, sync_session

DB = sync_DB_URL
from app.models.user import User

Session_Local = sync_session


def get_info(payload: dict):
    db = Session_Local()
    user_info = db.query(User).filter(User.id == payload['id']).first()
    if user_info is None:
        raise HTTPException(status_code=404, detail="Not Found")
    user_info.card_number = changes_cart(user_info.card_number)
    return {
        "username": user_info.username,
        "email": user_info.email,
        "phone": user_info.phone,
        "name": user_info.name,
        "lastname": user_info.lastname,
        "cart_number": user_info.card_number
    }


def changes_cart(cart: int):
    cart = str(cart)
    new_cart = ""
    for i in range(0, 16):
        if (len(cart) >= i + 1):
            print(i)
            if i >= 4:
                new_cart += '*'
            else:
                new_cart += cart[i]
    return new_cart
