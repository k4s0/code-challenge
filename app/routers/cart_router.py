from fastapi import APIRouter
from app.dto.cart_dto import CartSchemaDto
from app.dto.item_dto import ItemSchemaDto
from app.schemas.cart_schema import CartSchema
from app.schemas.item_schema import ItemSchema
from app.services.cart_services import CartService

cart_router = APIRouter(
  tags=['Cart']
)

@cart_router.get('/{customer_id}')
def view_cart(customer_id:int):
  cart_service = CartService()
  return cart_service.ViewCart(customer_id)

@cart_router.post('/create')
def create_cart(param: CartSchemaDto):
  cart_service = CartService()
  result = cart_service.CreateCart(CartSchema(
  ecommerce_id=param.ecommerce_id,
  customer_id=param.customer_id,
  status=param.status,
  created_at=param.created_at,
  updated_at=param.updated_at
  ))
  return result
  
@cart_router.post('/checkout/{customer_id}')
def checkout_cart(customer_id:int):
  cart_service = CartService()
  result = cart_service.CheckoutCart(customer_id)
  return result

@cart_router.post('/add/')
def add_item_to_cart(param: ItemSchemaDto):
  cart_service = CartService()
  result = cart_service.AddCart(ItemSchema(
    ecommerce_id=param.ecommerce_id,
    customer_id=param.customer_id,
    item_list=param.item_list
  ))
  return result