

from dataclasses import dataclass
from app.schemas.cart_schema import CartSchema
from app.sql_query.Query import Query

"""
For testing purpose this class not implementing a real database connection, but only return fake_db_data
"""
class CartModel():

  def InsertNewCart(self,input: CartSchema):
    #Insert the CartSchema class into database for the current customer
    #{......}
    return "Cart created for customer "+ str(input.customer_id)

  def GetCartCheckoutDate(self,customer_id:int):
    #Get customer cart checkout date from database using the customer_id
    #{......}
    #Create fake_db_data
    result=None
    if customer_id == 1:
      result = Query.sql_get_fake_db_data_1()
    return result["cart_date_checkout"]
  
  def GetCart(self,customer_id:int):
    #Get customer cart from database using the customer_id
    #{......}
    #Create fake_db_data
    result=None
    if customer_id == 1:
      result = Query.sql_get_fake_db_data_1()
    return result
    
  def CheckoutCart(self,customer_id:int):
    #Set the cart date_checkout to the current datetime and return the final price for the cart
    #{......}
    #Rerun fake_db_data
    return customer_id

  def InsertItem(self,input: CartSchema):
    #Insert the input items into the customer cart
    #{......}
    return input