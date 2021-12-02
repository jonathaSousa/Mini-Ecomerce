from typing import List
from fastapi import APIRouter,Depends,status
from starlette.status import HTTP_201_CREATED

from app.models.models import Product
from .schemas import CategoriesSchema, ShowCategorieSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)

def create(product: CategoriesSchema, db: Session = Depends(get_db)):
    db.add(Product(**product.dict()))
    db.commit()

@router.get('/', response_model=List[ShowCategorieSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.put('/{id}')
def update(id: int, product: CategoriesSchema):
    def update(id: int, product: CategoriesSchema, db: Session = Depends(get_db)):
        query = db.query(product).filter_by(id=id)
        query.update(product,dict())
        db.commit()


@router.get('/{id', response_model=List[ShowCategorieSchema])
def show(id: int,db: Session = Depends(get_db)):
    return db.query(Product).filter_by(id=id).first()
    