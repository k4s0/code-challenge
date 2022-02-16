from fastapi import FastAPI
from app.routers.cart_router import cart_router

app = FastAPI()

app.include_router(cart_router, prefix="/cart")