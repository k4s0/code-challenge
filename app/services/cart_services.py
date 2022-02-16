import pandas as pd
from app.models.cart_model import CartModel
from app.schemas.cart_schema import CartSchema
from app.schemas.item_schema import ItemSchema
from datetime import datetime, timedelta

class CartService():
  def __init__(self):
    self.model = CartModel()

  def __discount_percentage(whole,discount):
    percent = 1
    if discount == "5":
      percent = 5
    if discount == "10":
      percent = 10
    if discount == "15":
      percent = 15
    if discount == "20":
      percent = 20
    if percent == 1:
      return whole
    else:
      result = (percent * whole) / 100.0
      return whole - result  

  def __mime_percentage(whole,mime):
    percent = 1
    if mime == "pdf":
      percent = 15
    if mime == "psd":
      percent = 35
    if mime == "ai":
      percent = 25
    if percent == 1:
      return whole
    else:
      result = (percent * whole) / 100.0
      return whole + result

  def __delivery_date_percentage(whole,date,cart_date):
    percent = 1
    if (date.replace(tzinfo=None) - cart_date ) <= timedelta(1):
      percent = 30
    if (date.replace(tzinfo=None) - cart_date) > timedelta(1) and (date.replace(tzinfo=None) - cart_date) <= timedelta(2):
      percent = 20
    if (date.replace(tzinfo=None) - cart_date) > timedelta(2) and (date.replace(tzinfo=None)- cart_date ) <= timedelta(3):
      percent = 10
    if (date.replace(tzinfo=None) - cart_date) >= timedelta(7):
      return whole
    elif percent == 1:
      return whole
    else:
      result = (percent * whole) / 100.0
      return whole + result

  def CreateCart(self, input: CartSchema):
    return self.model.InsertNewCart(input)

  def ViewCart(self, customer_id:int):
    #Get cart for the current customer
    cart = self.model.GetCart(customer_id)
    #Map cart into array of all product_sku to apply discount polices
    res = (pd.DataFrame(cart["item_list"])
      .groupby(['product_sku'], as_index=False)
      .quantity.sum()
      .to_dict('r'))
      
    #Applying the price polices discout for the quantity of each item
    for i in range(len(cart["item_list"])):
      for j in range(len(res)):
        if cart["item_list"][i]["product_sku"] == res[j]["product_sku"]:
          if res[j]["quantity"] >= 100 and res[j]["quantity"] < 250:
            cart["item_list"][i]["price"] = CartService.__discount_percentage(cart["item_list"][i]["price"],"5")
          if res[j]["quantity"] >= 250 and res[j]["quantity"] < 500:
            cart["item_list"][i]["price"] = CartService.__discount_percentage(cart["item_list"][i]["price"],"10")
          if res[j]["quantity"] >= 500 and res[j]["quantity"] < 1000:
            cart["item_list"][i]["price"] = CartService.__discount_percentage(cart["item_list"][i]["price"],"15")
          if res[j]["quantity"] >= 1000:
            cart["item_list"][i]["price"] = CartService.__discount_percentage(cart["item_list"][i]["price"],"20")
            
    return cart
    
  def AddCart(self, input: ItemSchema):
    #Get cart_checkout_date for the current customer
    cart_checkout_date = self.model.GetCartCheckoutDate(input.customer_id)
    date_time_obj = datetime.strptime(cart_checkout_date, '%Y-%m-%d')

    #Check for price polices before insert the items
    for i in range(len(input.item_list)):
      #Store the current price
      current_price = input.item_list[i].price
      #Calculate mime_type percentage 
      input.item_list[i].price = CartService.__mime_percentage(input.item_list[i].price,input.item_list[i].file_type)
      #Calculate delivery date percentage
      input.item_list[i].price += CartService.__delivery_date_percentage(current_price,input.item_list[i].delivery_date,date_time_obj)
    
    return self.model.InsertItem(input)
  
  def CheckoutCart(self,customer_id:int):
    return self.model.CheckoutCart(customer_id)