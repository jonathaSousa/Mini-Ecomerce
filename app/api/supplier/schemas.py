from pydantic import BaseModel
from sqlalchemy import orm

class SuppliersSchema(BaseModel):
    name: str
    cnpj: str
class ShowSuppliersSchema(SuppliersSchema):
    id: int 
    class Config:
        orm_mode = True
