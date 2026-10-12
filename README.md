# Chocolate Store E-commerce Application

A full-stack premium chocolate store built with FastAPI, PostgreSQL, and React.

## Features
- Customer shopping experience with catalog, cart, checkout, and order tracking
- JWT authentication for customers and admin
- Admin dashboard for products and sales summary
- PostgreSQL-backed data model
- Swagger UI for API documentation
- Docker setup for local environment

## Stack
- Backend: Python, FastAPI, SQLAlchemy, PostgreSQL
- Frontend: React, Vite, CSS
- Auth: JWT
- Payment: Stripe-ready test-mode integration for future extension

## Local setup

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

### Database
Create a PostgreSQL database named `chocolate_store` and ensure your DATABASE_URL matches it.

### Docker
```bash
docker compose up --build
```

### Swagger
Visit `http://localhost:8000/docs`

## Default admin account
- Email: `admin@chocolateshop.com`
- Password: `admin123`

## Notes
- The frontend connects to the backend via `VITE_API_URL`.
- This project is built as a working MVP for a chocolate e-commerce application.
