from datetime import datetime
from typing import List

class Items():
    product_sku:int
    product_name:str
    file_type:str
    quantity:int
    delivery_date:datetime
    price:float = 1.0

class ItemSchema():
  ecommerce_id:int
  customer_id:int
  item_list: List[Items]
  
  def __init__(self,
    ecommerce_id: int,
    customer_id: int,
    item_list: List[Items]):

    self.ecommerce_id = ecommerce_id
    self.customer_id = customer_id
    self.item_list = item_list

