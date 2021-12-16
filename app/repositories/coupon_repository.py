from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Coupon
from .base_repository import BaseRepository
from fastapi import Depends


class CouponRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Coupon)
    
    def has_coupon(self, code):
        query = self.session.query(self.model).filter_by(code=code).first()
        return query != None
    
    def remove(self, id):
        self.query().filter_by(id=id).delete()
   