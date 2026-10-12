# Chocolate Store E-commerce Application

A full-stack chocolate store web app built with FastAPI and React.

## Features
- Product catalog with filtering and search
- Shopping cart and wishlist
- JWT auth and admin access
- Orders and checkout flow
- Swagger API docs
- PostgreSQL + SQLAlchemy

## Stack
- Backend: Python, FastAPI, SQLAlchemy, PostgreSQL
- Frontend: React, Vite, CSS
- Auth: JWT

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env
npm run dev -- --host 0.0.0.0 --port 5173
```

### Docker
```bash
docker compose up --build
```

## Swagger
Open `http://localhost:8000/docs`

## Default admin
- Email: `admin@chocolateshop.com`
- Password: `admin123`

## Notes
This is a working MVP suitable for local development and extension.
