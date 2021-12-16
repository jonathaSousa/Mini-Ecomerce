from fastapi import APIRouter, Depends,status
from app.models.models import PaymentMethod
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from app.repositories.payment_method import PaymentMethodRepository
from  typing import List


from app.services.auth_service import get_user, only_admin
router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(payment_method:PaymentMethodSchema,repository: PaymentMethodRepository = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))

@router.get('/',response_model=List[ShowPaymentMethodSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()
    

@router.put('/{id}')
def update(id:int,payment_method:PaymentMethodSchema,repository: PaymentMethodRepository = Depends()):
     repository.update(id,payment_method.dict())


@router.get('/{id}')
def show(id:int, repository: PaymentMethodRepository = Depends()):
    return repository.get_by_id(id)