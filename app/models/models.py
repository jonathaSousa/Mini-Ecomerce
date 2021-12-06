from app.db.db import Base

from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, Integer, String
from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship




class Customer (Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(45))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(String)

    #user_id = Column(Integer, ForeignKey('users.id'))
    #user = relationship(User)
   

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship(Supplier)
    created_at = Column(DateTime)


class PaymentMethod(Base):
    __tablename__ = 'payment_methods'
    name = Column(Integer, primary_key=True)
    enabled = Column(Boolean,default=True)


class ProductDiscount(Base):
    __tablename__ = 'product_discounts'
    id = Column(Integer, primary_key=True)

    product_id = Column(Integer,ForeignKey('products.id'))
    product = relationship(Product)

    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'))
    payment_method = relationship(PaymentMethod)

#class User(Base):
 #   __tablename__ = 'users'
  #  id = Column(Integer, primary_key=True)
   # display_name = Column(String(45))
    #email = Column(String(45))
    #phone_number = Column(String(12))
    #role = Column(String(15))
    #password = Column(String(255))

class Customer (Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(45))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(String)

    #user_id = Column(Integer, ForeignKey('users.id'))
    #user = relationship(User)
   
class Addresse(Base):
    __tablename__ = 'adresses'
    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zip = Column(String(10))
    neighbourhood = Column(String(45))
    primary = Column(Boolean, default=True)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customer)

class Coupon(Base):
    __tablename__ = 'coupons'
    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    expite_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float(10,2))
    

