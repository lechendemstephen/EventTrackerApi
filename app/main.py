from fastapi import FastAPI

from .routers import events, users 
from .database import engine
from . import models

Base = models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# creating insances for the user and event routers 
app.include_router(users.router)
app.include_router(events.router)


