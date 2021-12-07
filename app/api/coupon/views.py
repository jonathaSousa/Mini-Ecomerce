from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Coupon
from .schemas import CouponSchema, ShowCouponSchema, UpdateCouponSchema
from app.repositories.coupon_repository import CouponRepository
from app.services.coupon_service import CouponService

from app.services.auth_service import only_admin

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, repository: CouponRepository = Depends()):
    #repository.create(Coupon(**coupon.dict()))
    CouponService.create_coupon(Coupon(**Coupon.dict()))

@router.get('/', response_model=List[ShowCouponSchema])
def index(repository: CouponRepository = Depends()):
    return repository.get_all()

@router.get('/{id}', response_model=ShowCouponSchema)
def show(id: int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)


@router.put('/{id}')
def update(id: int, coupon: UpdateCouponSchema, repository: CouponRepository = Depends()):   
    CouponService.update_coupon(id, coupon)

