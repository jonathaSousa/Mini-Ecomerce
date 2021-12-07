from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from app.repositories.product_discount import ProductDiscountRepository
from app.models.models import ProductDiscount
from .schemas import ProductDiscountSchema, ShowProductDiscountSchema
from app.services.product_discount_service import ProductDiscountService
from app.services.auth_service import only_admin

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, repository: ProductDiscountRepository = Depends()):
    ProductDiscountService.create_discount(product_discount)

@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
  
    ProductDiscountService.listar()