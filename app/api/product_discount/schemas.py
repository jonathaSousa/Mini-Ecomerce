
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import orm
from enum import Enum
from app.api.product.schemas import ShowProductSchema
from app.api.payment_method.schemas import ShowPaymentMethodSchema


class DiscountMode(str,Enum):
    VALUE = 'value'
    PERCENTAGEM = 'percentage'

class ProductDiscountSchema(BaseModel):
    mode: DiscountMode
    value: float
    product_id: int
    payment_method_id:int

class ShowProductDiscountSchema( ProductDiscountSchema):
    id: int
    product:ShowProductSchema
    payment_method:ShowPaymentMethodSchema
    class Config:
        orm_mode = True