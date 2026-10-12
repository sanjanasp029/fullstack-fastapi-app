# Detailed Setup Instructions

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)
4. [Database Setup](#database-setup)
5. [Docker Setup](#docker-setup)
6. [Verification](#verification)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software
- **Git**: For cloning the repository
- **Python 3.11+**: For backend
- **Node.js 18+**: For frontend
- **PostgreSQL 15+**: For database
- **Docker & Docker Compose**: (Optional, but recommended)

### Installation Verification

```bash
# Check Python version
python --version  # Should be 3.11 or higher

# Check Node version
node --version    # Should be 18 or higher
npm --version

# Check PostgreSQL version
psql --version    # Should be 15 or higher

# Check Docker (if using Docker)
docker --version
docker compose version
```

## Backend Setup

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create Python Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
# Copy example file
cp .env.example .env

# Edit .env with your settings
nano .env  # or use your editor
```

**Key variables to set**:
```env
SECRET_KEY=change-this-to-a-long-random-string
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/chocolate_store
```

### Step 5: Initialize Database

```bash
# Create database (if not exists)
psql -U postgres -c "CREATE DATABASE chocolate_store;"

# Run Alembic migrations
alembic upgrade head

# Seed sample data
python app/db/init_db.py
```

### Step 6: Start Backend Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000

Swagger documentation: http://localhost:8000/docs

## Frontend Setup

### Step 1: Navigate to Frontend Directory

```bash
cd frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Configure Environment Variables

```bash
# Copy example file
cp .env.example .env

# Update VITE_API_URL if backend is on different port
echo "VITE_API_URL=http://localhost:8000" >> .env
```

### Step 4: Start Development Server

```bash
npm run dev
```

Frontend will be available at: http://localhost:5173

## Database Setup

### Manual PostgreSQL Setup

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE chocolate_store;

# Create user (optional, for security)
CREATE USER chocolate_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE chocolate_store TO chocolate_user;

# Exit psql
\q
```

### Run Migrations

```bash
cd backend

# Create migration for new changes (if needed)
alembic revision --autogenerate -m "Initial schema"

# Apply all migrations
alembic upgrade head

# View migration status
alembic current
```

### Seed Database with Sample Data

```bash
cd backend
python app/db/init_db.py
```

This creates:
- Admin user (admin@chocolateshop.com / admin123)
- Sample customer
- Sample categories
- Sample products
- Sample reviews
- Sample coupons

## Docker Setup

### Step 1: Configure Environment

```bash
cp .env.example .env
```

### Step 2: Build and Start Services

```bash
# Build images and start all services
docker compose up --build

# Run in background
docker compose up -d --build
```

### Step 3: Initialize Database (one-time setup)

```bash
# Wait for services to start (about 30 seconds)

# Run migrations
docker exec chocolate-store-backend alembic upgrade head

# Seed database
docker exec chocolate-store-backend python app/db/init_db.py
```

### Services Running

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432

### Docker Compose Commands

```bash
# View logs
docker compose logs -f

# View specific service logs
docker compose logs -f backend
docker compose logs -f frontend

# Stop services
docker compose down

# Remove volumes (reset database)
docker compose down -v

# Restart services
docker compose restart

# Execute command in container
docker exec chocolate-store-backend bash
```

## Verification

### Backend Health Check

```bash
# Check if API is running
curl http://localhost:8000/health

# Should return:
# {"status": "healthy"}
```

### Frontend Connection

1. Open http://localhost:5173
2. Should see the chocolate store homepage
3. Check browser console for any API errors

### Database Connection

```bash
# From backend directory
python -c "from app.db.session import engine; print('✓ Database connected')"
```

### Test User Login

1. Go to http://localhost:5173
2. Click "Login"
3. Use default credentials:
   - Email: `customer@example.com`
   - Password: `customer123`
4. Should successfully log in

### Test Admin Access

1. Log in with admin credentials:
   - Email: `admin@chocolateshop.com`
   - Password: `admin123`
2. Access admin dashboard at http://localhost:5173/admin

## Running Tests

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=app tests/

# Run specific test file
pytest tests/test_auth.py -v

# Run specific test
pytest tests/test_auth.py::test_user_registration -v
```

### Frontend Tests (Optional)

```bash
cd frontend

# Run tests (if test setup is configured)
npm test
```

## Troubleshooting

### Backend Issues

**"ModuleNotFoundError: No module named 'app'"**
- Ensure you're in the `backend` directory
- Activate virtual environment: `source .venv/bin/activate`
- Reinstall requirements: `pip install -r requirements.txt`

**"Error: Could not connect to database"**
- Check PostgreSQL is running: `sudo systemctl status postgresql`
- Verify DATABASE_URL in .env is correct
- Ensure database exists: `psql -l`

**"Error: Secret key not set"**
- Set SECRET_KEY in .env
- Example: `openssl rand -hex 32`

### Frontend Issues

**"Cannot GET /"**
- Ensure you're in `frontend` directory
- Check `npm run dev` output for errors
- Clear .vite cache: `rm -rf node_modules/.vite`

**"Failed to fetch from API"**
- Check VITE_API_URL in frontend .env
- Ensure backend is running on correct port
- Check browser console for CORS errors

### Database Issues

**"FATAL: role 'postgres' does not exist"**
- Install PostgreSQL properly or create the role
- `sudo -u postgres createuser postgres`

**"Database 'chocolate_store' does not exist"**
- Create it: `psql -U postgres -c "CREATE DATABASE chocolate_store;"`
- Or let the app create it automatically

### Docker Issues

**"Cannot bind to port 8000"**
- Port is in use
- Change port in docker-compose.yml
- Or kill process: `lsof -ti:8000 | xargs kill -9`

**"Database connection failed in container"**
- Check `POSTGRES_SERVER=db` (not localhost)
- Ensure db service is healthy: `docker compose ps`
- Wait longer for db to initialize: `sleep 20`

**"Frontend can't reach backend in container"**
- VITE_API_URL should be `http://localhost:8000` (from browser)
- Not `http://backend:8000` (that's internal container URL)

## Development Workflow

### Making Changes

```bash
# Backend changes (with reload)
uvicorn app.main:app --reload

# Frontend changes (with HMR)
npm run dev

# Database schema changes
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

### Creating New Models

1. Define model in `app/models/`
2. Define schema in `app/schemas/`
3. Create migration: `alembic revision --autogenerate -m "Add new model"`
4. Apply migration: `alembic upgrade head`
5. Create API endpoints in `app/api/v1/endpoints/`

### API Development

1. Test endpoints with Swagger UI: http://localhost:8000/docs
2. Or use curl/Postman
3. Check logs in backend console
4. Verify database changes

## Next Steps

1. **Customize**: Update branding, colors, and product images
2. **Configure Stripe**: Add real test keys in .env
3. **Deploy**: Use provided Docker setup for production
4. **Scale**: Set up database backups and monitoring
5. **Optimize**: Add caching, CDN, and performance improvements

## Getting Help

- Check logs: `docker compose logs -f service_name`
- Read FastAPI docs: https://fastapi.tiangolo.com
- Check React docs: https://react.dev
- PostgreSQL docs: https://www.postgresql.org/docs
