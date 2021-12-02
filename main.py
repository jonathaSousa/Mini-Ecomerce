from fastapi import FastAPI
from app.db.db import engine 
from app.api.router import router
from app.models.models import Base

 
Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(router)