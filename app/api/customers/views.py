from typing import List
from fastapi import APIRouter, Depends , status
from fastapi.exceptions import HTTPException
from app.models.models import Customer
from app.repo.customer_repo import CustomerRepository
from .schemas import CustomerSchema, ShowCustomerSchema, UpdateCustomerSchema



router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(customer: CustomerSchema, repository: CustomerRepository = Depends()):
    repository.create(Customer(**customer.dict()))
    


@router.get('/', response_model= List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id:int,customer:UpdateCustomerSchema, repository: CustomerRepository = Depends()):
    if customer is None:
        raise http_error()
    repository.update(id,customer.dict())



@router.get('/{id}')
def show(id:int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)


def http_error():
    return HTTPException(status_code=404, detail="not found customer")
