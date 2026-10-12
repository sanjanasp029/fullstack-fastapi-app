# Chocolate Store E-commerce Application

A complete, modern, responsive full-stack e-commerce web application for a premium chocolate store. Built with React, FastAPI, PostgreSQL, and integrated payment processing.

## Features

### Customer Features
- Browse and search premium chocolates
- Filter by category, price, brand, and ratings
- Product details with reviews and ratings
- Shopping cart with quantity management
- Wishlist functionality
- Secure checkout with address management
- Payment integration (Stripe test mode)
- Order tracking and history
- User account management
- Password reset and security

### Admin Features
- Dashboard with sales analytics
- Product management (CRUD operations)
- Inventory tracking with low-stock alerts
- Category and brand management
- Customer management
- Order management and fulfillment
- Coupon and promotion management
- Sales reports and analytics

## Technology Stack

### Backend
- **Framework**: FastAPI 0.104+
- **Language**: Python 3.11+
- **ORM**: SQLAlchemy 2.0+
- **Database**: PostgreSQL 15+
- **Authentication**: JWT (PyJWT)
- **Validation**: Pydantic v2
- **Password Hashing**: Passlib + Bcrypt
- **API Docs**: Swagger UI & ReDoc
- **Testing**: Pytest
- **Payment**: Stripe API (test mode)

### Frontend
- **Framework**: React 18+
- **Build Tool**: Vite
- **Styling**: CSS3 + Bootstrap 5
- **State Management**: React Context API
- **HTTP Client**: Axios
- **Routing**: React Router v6

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Database**: PostgreSQL 15 Alpine

## Project Structure

```
chocolate-store/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── core/
│   │   │   ├── config.py           # Settings and configuration
│   │   │   ├── security.py         # JWT and password hashing
│   │   │   └── constants.py        # Constants and enums
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── router.py       # API router
│   │   │       └── endpoints/
│   │   │           ├── auth.py     # Authentication endpoints
│   │   │           ├── users.py    # User management
│   │   │           ├── products.py # Product CRUD
│   │   │           ├── categories.py # Category management
│   │   │           ├── cart.py     # Shopping cart
│   │   │           ├── wishlist.py # Wishlist
│   │   │           ├── orders.py   # Orders
│   │   │           ├── payments.py # Payments
│   │   │           ├── admin.py    # Admin dashboard
│   │   │           └── reviews.py  # Product reviews
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # User model
│   │   │   ├── product.py          # Product and related models
│   │   │   ├── order.py            # Order models
│   │   │   ├── cart.py             # Cart model
│   │   │   ├── review.py           # Review model
│   │   │   └── base.py             # Base model class
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # User schemas
│   │   │   ├── product.py          # Product schemas
│   │   │   ├── order.py            # Order schemas
│   │   │   ├── cart.py             # Cart schemas
│   │   │   ├── review.py           # Review schemas
│   │   │   └── common.py           # Common schemas
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py     # User business logic
│   │   │   ├── product_service.py  # Product business logic
│   │   │   ├── order_service.py    # Order business logic
│   │   │   ├── payment_service.py  # Payment processing
│   │   │   ├── cart_service.py     # Cart business logic
│   │   │   └── coupon_service.py   # Coupon validation
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── base.py             # Base repository class
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── session.py          # Database session
│   │   │   ├── base.py             # Base for all models
│   │   │   └── init_db.py          # Database initialization
│   │   ├── dependencies/
│   │   │   └── auth.py             # Auth dependencies
│   │   ├── middleware/
│   │   │   └── error_handler.py    # Global error handling
│   │   └── utils/
│   │       ├── email.py            # Email utilities
│   │       ├── validators.py       # Custom validators
│   │       └── pagination.py       # Pagination utilities
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py             # Pytest configuration
│   │   ├── test_auth.py
│   │   ├── test_products.py
│   │   ├── test_orders.py
│   │   ├── test_cart.py
│   │   └── test_admin.py
│   ├── alembic/                    # Database migrations
│   │   ├── versions/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── alembic.ini
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env.example
│   └── .dockerignore
├── frontend/
│   ├── public/
│   │   ├── favicon.ico
│   │   └── images/
│   │       ├── hero-banner.jpg
│   │       └── placeholder.jpg
│   ├── src/
│   │   ├── main.jsx                # React entry point
│   │   ├── App.jsx                 # Main app component
│   │   ├── components/
│   │   │   ├── Layout/
│   │   │   │   ├── Navbar.jsx
│   │   │   │   ├── Footer.jsx
│   │   │   │   └── Sidebar.jsx
│   │   │   ├── Common/
│   │   │   │   ├── LoadingSpinner.jsx
│   │   │   │   ├── Modal.jsx
│   │   │   │   ├── Toast.jsx
│   │   │   │   └── Pagination.jsx
│   │   │   ├── Products/
│   │   │   │   ├── ProductCard.jsx
│   │   │   │   ├── ProductGrid.jsx
│   │   │   │   └── FilterSidebar.jsx
│   │   │   ├── Cart/
│   │   │   │   ├── CartItem.jsx
│   │   │   │   └── CartSummary.jsx
│   │   │   ├── Checkout/
│   │   │   │   ├── ShippingForm.jsx
│   │   │   │   ├── PaymentForm.jsx
│   │   │   │   └── OrderSummary.jsx
│   │   │   └── Admin/
│   │   │       ├── ProductForm.jsx
│   │   │       ├── OrderTable.jsx
│   │   │       └── AnalyticsCard.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Shop.jsx
│   │   │   ├── ProductDetail.jsx
│   │   │   ├── Cart.jsx
│   │   │   ├── Checkout.jsx
│   │   │   ├── OrderConfirmation.jsx
│   │   │   ├── Orders.jsx
│   │   │   ├── Profile.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── PasswordReset.jsx
│   │   │   ├── Admin/
│   │   │   │   ├── Dashboard.jsx
│   │   │   │   ├── ProductManagement.jsx
│   │   │   │   ├── OrderManagement.jsx
│   │   │   │   ├── CustomerManagement.jsx
│   │   │   │   └── Analytics.jsx
│   │   │   └── NotFound.jsx
│   │   ├── services/
│   │   │   ├── api.js            # API client (Axios)
│   │   │   ├── auth.js           # Auth service
│   │   │   ├── products.js       # Product service
│   │   │   ├── orders.js         # Order service
│   │   │   └── admin.js          # Admin service
│   │   ├── hooks/
│   │   │   ├── useAuth.js        # Auth hook
│   │   │   ├── useCart.js        # Cart hook
│   │   │   ├── useFetch.js       # Fetch hook
│   │   │   └── useForm.js        # Form hook
│   │   ├── context/
│   │   │   ├── AuthContext.jsx   # Auth context
│   │   │   ├── CartContext.jsx   # Cart context
│   │   │   └── ThemeContext.jsx  # Theme context
│   │   ├── styles/
│   │   │   ├── index.css         # Global styles
│   │   │   ├── variables.css     # CSS variables
│   │   │   ├── components.css    # Component styles
│   │   │   └── layouts.css       # Layout styles
│   │   └── utils/
│   │       ├── constants.js      # Constants
│   │       ├── validators.js     # Form validators
│   │       └── helpers.js        # Utility functions
│   ├── index.html
│   ├── vite.config.js
│   ├── .env.example
│   ├── package.json
│   ├── Dockerfile
│   └── .dockerignore
├── docker-compose.yml
├── .env.example
├── .gitignore
└── SETUP.md                        # Detailed setup instructions
```

## Quick Start

### Prerequisites
- Docker & Docker Compose (recommended)
- OR: Python 3.11+, Node.js 18+, PostgreSQL 15+

### Using Docker Compose (Recommended)

```bash
# Clone repository
git clone <repo-url>
cd chocolate-store

# Configure environment
cp .env.example .env

# Build and start all services
docker compose up --build

# In another terminal, seed the database
docker exec chocolate-store-backend python app/db/init_db.py
```

Application will be available at:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Manual Setup (Without Docker)

See [SETUP.md](./SETUP.md) for detailed instructions.

## Default Credentials

After seeding the database:

**Admin Account**
- Email: `admin@chocolateshop.com`
- Password: `admin123`

**Test Customer**
- Email: `customer@example.com`
- Password: `customer123`

## Environment Configuration

Copy `.env.example` to `.env` and update values:

```env
# Application
PROJECT_NAME=ChocolateStore
ENVIRONMENT=development
DEBUG=true

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/chocolate_store
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=chocolate_store

# Frontend
FRONTEND_URL=http://localhost:5173
VITE_API_URL=http://localhost:8000

# Stripe (Test Mode)
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...

# Email (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

All endpoints are documented with request/response examples.

## Testing

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_auth.py -v
```

## Key Workflows

### Customer Registration & Login
1. User registers with email, password, name, and phone
2. Password is hashed with bcrypt
3. User logs in and receives JWT access token
4. Token stored in localStorage (frontend)
5. Protected endpoints require valid token

### Product Browsing
1. Frontend fetches products with pagination
2. Products filtered by category, price range, rating
3. Search across product names and descriptions
4. Product details include images, ingredients, allergens

### Shopping Cart
1. Add/remove items from cart
2. Backend validates stock availability
3. Cart persisted in database (for authenticated users)
4. Totals calculated server-side (never trust frontend)

### Checkout & Payment
1. Select shipping address
2. Apply coupon code (validated on backend)
3. Review order summary
4. Create Stripe payment session
5. Stripe processes payment in test mode
6. Webhook confirms payment
7. Order created with "Confirmed" status
8. Inventory updated

### Admin Dashboard
1. Admin logs in with elevated permissions
2. Access product management, orders, customers, analytics
3. Add/edit products with images and details
4. Manage inventory with low-stock alerts
5. Update order statuses
6. View sales analytics and reports

## Database Schema Highlights

- **Users**: Customer and admin accounts
- **Products**: Chocolate items with prices, stock, descriptions
- **Categories**: Chocolate types (Dark, Milk, White, etc.)
- **CartItems**: Shopping cart with quantities
- **Orders**: Complete order records with status tracking
- **OrderItems**: Order line items with price snapshots
- **Payments**: Payment records with Stripe transaction IDs
- **Reviews**: Customer ratings and reviews
- **Coupons**: Promotional codes with usage tracking
- **InventoryMovements**: Stock adjustment history

## Security Features

✅ JWT-based authentication
✅ Password hashing with Bcrypt
✅ Role-based access control (RBAC)
✅ CORS configured for frontend origin
✅ Input validation with Pydantic
✅ SQL injection prevention (SQLAlchemy ORM)
✅ Secure password reset tokens
✅ Protected payment and admin endpoints
✅ Environment-based secrets management
✅ No sensitive data in logs
✅ Stripe API key security

## Performance Considerations

- Database indexes on frequently queried columns
- Pagination for large datasets
- Product filtering and sorting at database level
- Efficient image handling with CDN-ready structure
- API response caching where appropriate
- Connection pooling for database

## Deployment

For production deployment:

1. Set `ENVIRONMENT=production`
2. Generate strong `SECRET_KEY`
3. Use production PostgreSQL instance
4. Configure Stripe production keys
5. Set `FRONTEND_URL` and `CORS_ORIGINS` correctly
6. Enable HTTPS
7. Use environment secrets management (AWS Secrets Manager, etc.)
8. Configure database backups
9. Set up monitoring and logging
10. Deploy with a production ASGI server (Gunicorn, etc.)

## Troubleshooting

**Port already in use**: Change ports in `.env` or `docker-compose.yml`

**Database connection error**: Verify PostgreSQL is running and credentials are correct

**Frontend can't reach backend**: Check `VITE_API_URL` and CORS configuration

**Payment errors**: Verify Stripe keys are correct and in test mode

**Authentication issues**: Ensure `SECRET_KEY` is set and consistent

## Contributing

Follow the project structure and existing patterns. Ensure tests pass before submitting.

## License

MIT License - See LICENSE file

## Support

For issues and questions, open a GitHub issue or contact the development team.
