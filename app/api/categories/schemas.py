from pydantic import BaseModel
from sqlalchemy import orm

class CategoriesSchema(BaseModel):
    name: str
    description: str
class ShowCategorieSchema(CategoriesSchema):
    id: int 
    class Config:
        orm_mode = True
