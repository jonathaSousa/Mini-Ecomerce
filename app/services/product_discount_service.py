from fastapi import Depends
from app.common.exceptions import PaymentMethodDiscountAlreadyExistsException, PaymentMethodsNotAvailableException
from app.models.models import ProductDiscount
from app.repositories.payment_method import PaymentMethodRepository
from app.repositories.product_discount import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema


class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, discount: ProductDiscountSchema):
        self._validate_payment_method(discount.payment_method_id, discount.product_id)

        self.product_discount_repository.create(
            ProductDiscount(**discount.dict()))

    def update_discount(self, id, discount: ProductDiscountSchema):
        self._validate_payment_method(
            discount.payment_method_id, discount.product_id, id)

        self.product_discount_repository.update(id, discount.dict())

    def _validate_payment_method(self, payment_method_id, product_id, ignored_id=None):
        payment_method = self.payment_method_repository.get_by_id(
            payment_method_id)

        if not payment_method or not payment_method.enabled:
            raise PaymentMethodsNotAvailableException()

        find_payment_method_existence = self.product_discount_repository.filter(
            {'product_id': product_id, 'payment_method_id': payment_method_id})

        if find_payment_method_existence and ignored_id != find_payment_method_existence[0].id:
            raise PaymentMethodDiscountAlreadyExistsException()