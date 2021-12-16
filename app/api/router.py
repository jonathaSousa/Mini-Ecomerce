from fastapi import APIRouter

from.product.views import router as product_router
from.supplier.views import router as supplier_router
from.category.views import router as category_router
from.product_discount.views import router as product_discount_router
from.coupon.views import router as coupon_router
from.address.views import router as address_router
from.customer.views import router as customer_router
from.payment_method.views import router as payment_method_router
from .seed import router as seed_router
from .auth.views import router as auth_router
from .user.views import router as user_router
from .order.views import router as order_router
from .catalog.views import router as catalog_router


router = APIRouter()

router.include_router(product_router,prefix='/product',tags=['product'])
router.include_router(supplier_router,prefix='/supplier',tags=['supplier'])
router.include_router(payment_method_router,prefix='/payment_method',tags=['payment_method'])
router.include_router(product_discount_router,prefix='/product_discount',tags=['product_discount'])
router.include_router(category_router,prefix='/category',tags=['category'])
router.include_router(address_router,prefix='/address',tags=['address'])
router.include_router(customer_router,prefix='/customer',tags=['customer'])
router.include_router(coupon_router,prefix='/coupon',tags=['coupon'])
router.include_router(seed_router, tags=['seed'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(user_router, prefix='/users', tags=['users'])
router.include_router(order_router, prefix='/orders', tags=['order'])
router.include_router(catalog_router, prefix='/catalog', tags=['catalog'])