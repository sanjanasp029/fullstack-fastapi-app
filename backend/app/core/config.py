from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_NAME = "ChocolateStore"
API_V1_STR = "/api/v1"
SECRET_KEY = "change-me-in-production-please-use-a-long-random-string"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/chocolate_store"
FRONTEND_URL = "http://localhost:5173"
CORS_ORIGINS = ["http://localhost:5173", "http://localhost:3000"]
STRIPE_API_KEY = ""
STRIPE_WEBHOOK_SECRET = ""
