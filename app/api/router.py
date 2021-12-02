from fastapi import FastAPI
from fastapi.routing import APIRouter
from .product.views import router as product_router


router = APIRouter()

router.include_router(product_router, prefix='/product')
router.include_router(product_router, prefix='/categories')
router.include_router(product_router, prefix='/suppliers')
router.include_router(product_router, prefix='/paymentmethods')
