# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from app.routers import ping #users, products# Initialize the app

app = FastAPI()
app.include_router(ping.router)

