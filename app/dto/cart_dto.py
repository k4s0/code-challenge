from datetime import datetime
from fastapi import Query
from pydantic import BaseModel, validator

class CartSchemaDto(BaseModel):
    __status = ["created","building","checkout"]
    ecommerce_id:int
    customer_id:int
    status: str = Query("created",enum=__status)
    created_at: datetime
    updated_at: datetime

    @validator('status')
    def status_validator(cls,v):
        if v not in CartSchemaDto.__status:
            raise ValueError('KO - status must be one of the given element ('+ ', '.join(CartSchemaDto.__status)+')')
        return v