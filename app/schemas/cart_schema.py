from datetime import datetime

class CartSchema():
  ecommerce_id:int
  customer_id:int
  status: str
  created_at: datetime
  updated_at: datetime
  
  def __init__(self,
    ecommerce_id: int,
    customer_id: int,
    status: str,
    created_at: datetime,
    updated_at: datetime):

    self.ecommerce_id = ecommerce_id
    self.customer_id = customer_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at

