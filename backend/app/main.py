from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import admin, auth, cart, orders, payments, products, users, wishlist
from app.api.v1.router import api_router
from app.core.config import settings
from app.db.init_db import init_db

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0", docs_url="/docs", redoc_url="/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/")
def root() -> dict:
    return {"message": "Chocolate Store API"}


app.include_router(api_router)
