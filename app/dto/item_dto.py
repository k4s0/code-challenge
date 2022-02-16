from datetime import date, datetime
from typing import List
from fastapi import Query
from pydantic import BaseModel, validator

class Items(BaseModel):
    __allowed_mime = ["application/pdf","image/vnd.adobe.photoshop"]
    __allowed_ext = ["pdf","psd","ai"]
    product_sku:int
    product_name:str
    file_type:str = Query("pdf",enum=__allowed_ext)
    quantity:int
    delivery_date:datetime
    price:float = 1.0
    
    @validator('file_type')
    def status_validator(cls,v):
        if v not in Items.__allowed_ext:
            raise ValueError('KO - file_type must be one of the given element ('+ ', '.join(Items.__allowed_ext)+')')
        return v

class ItemSchemaDto(BaseModel):
    ecommerce_id:int
    customer_id:int
    item_list: List[Items]
