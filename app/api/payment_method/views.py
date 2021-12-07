from typing import List
from fastapi import APIRouter, status
from fastapi import Depends

from app.repositories.payment_method import PaymentMethodRepository
from app.models.models import PaymentMethod
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from app.services.auth_service import only_admin

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodSchema, repository: PaymentMethodRepository = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))



@router.get('/', response_model=List[ShowPaymentMethodSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()

