# Cake House Backend API

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![Status](https://img.shields.io/badge/status-active-success)

Backend REST API for the **Cake House** e-commerce website. It manages products, authentication, user profiles, carts, wishlists, reviews, orders and multilingual product data.

## Features

- User registration and login
- Bearer token authentication
- Secure password hashing
- User profile updates
- Password changing
- PostgreSQL data persistence
- Product listing and detail endpoints
- Product search, filtering and sorting
- New arrival, best seller, top rated and limited edition products
- Related product suggestions
- English, Azerbaijani and Polish product content
- Persistent user wishlist
- Persistent user shopping cart
- Product quantity and size management
- Product review submission
- Automatic average product rating calculation
- Order creation and order history
- Automatic subtotal, VAT and total calculation
- Automatic cart clearing after checkout
- Request validation with Pydantic
- Interactive Swagger and ReDoc documentation
- Configurable CORS support

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | Database ORM |
| Pydantic | Request and response validation |
| Uvicorn | ASGI development server |
| psycopg2 | PostgreSQL database driver |
| PBKDF2-HMAC | Secure password hashing |
| Bearer Token | Protected endpoint authentication |

## Project Structure

```text
cake-house-backend/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── data/
│   │   ├── products.py
│   │   ├── reviews.py
│   │   └── users.py
│   ├── db_models/
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── product.py
│   │   ├── review.py
│   │   ├── user.py
│   │   └── wishlist.py
│   ├── models/
│   │   ├── auth.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── review.py
│   │   └── wishlist.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── cart.py
│   │   ├── orders.py
│   │   ├── products.py
│   │   ├── reviews.py
│   │   └── wishlist.py
│   ├── services/
│   │   └── products.py
│   └── database.py
├── database/
│   └── products_seed.sql
├── scripts/
│   └── seed_products.py
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

Before starting, install:

- Python 3.10 or newer
- PostgreSQL
- Git
- pip

## Installation

### 1. Clone the repository

```bash
git clone <backend-repository-url>
cd cake-house-backend
```

### 2. Create a virtual environment

Windows:

```powershell
py -m venv venv
venv\Scripts\activate
```

macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```powershell
py -m pip install -r requirements.txt
```

The project uses the following packages:

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
```

## PostgreSQL Setup

Open PostgreSQL SQL Shell (`psql`) and connect as the `postgres` administrator.

Create the application user and database:

```sql
CREATE USER cake_house_user
WITH PASSWORD 'cake_house_password';

CREATE DATABASE cake_house_db
OWNER cake_house_user;
```

Connect to the new database:

```sql
\c cake_house_db
```

Grant the required permissions:

```sql
GRANT USAGE, CREATE ON SCHEMA public TO cake_house_user;

GRANT ALL PRIVILEGES
ON ALL TABLES IN SCHEMA public
TO cake_house_user;

GRANT ALL PRIVILEGES
ON ALL SEQUENCES IN SCHEMA public
TO cake_house_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO cake_house_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON SEQUENCES TO cake_house_user;
```

List available databases:

```sql
\l
```

List the current database tables:

```sql
\dt
```

Exit SQL Shell:

```sql
\q
```

## Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE_NAME
SECRET_KEY=YOUR_SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES=1440
ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

### Environment variable reference

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection URL |
| `SECRET_KEY` | Secret used to sign access tokens |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Access token lifetime |
| `ORIGINS` | Comma-separated allowed frontend origins |

Generate a secure secret key:

```powershell
py -c "import secrets; print(secrets.token_urlsafe(48))"
```

Never commit the real `.env` file to GitHub.

## Database Tables

The backend automatically creates the required tables when it starts.

| Table | Description |
|---|---|
| `users` | Registered user accounts |
| `products` | Product information and translations |
| `wishlist_items` | Products saved by users |
| `cart_items` | User cart products, sizes and quantities |
| `reviews` | Product reviews and ratings |
| `orders` | Customer order and billing information |
| `order_items` | Products belonging to an order |

## Seed Products

Product data can be inserted using the Python seed script:

```powershell
py scripts/seed_products.py
```

The script:

- Creates missing tables
- Inserts new products
- Updates existing products by ID
- Includes English, Azerbaijani and Polish fields
- Preserves product images, tags, sizes and flags

Alternatively, import the SQL seed file:

```sql
\i 'C:/full/path/to/cake-house-backend/database/products_seed.sql'
```

Use forward slashes in the SQL file path on Windows.

## Running the Server

Start the development server:

```powershell
uvicorn main:app --reload
```

If `uvicorn` is not recognized:

```powershell
py -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Health response:

```text
GET http://127.0.0.1:8000/
```

```json
{
  "message": "Cake shop API is working"
}
```

## API Documentation

FastAPI generates interactive documentation automatically:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Authentication

Protected endpoints require an access token:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Register example

```http
POST /auth/register
Content-Type: application/json
```

```json
{
  "fullName": "Nihad Memmedzade",
  "email": "nihad@example.com",
  "password": "securePassword123"
}
```

### Login example

```http
POST /auth/login
Content-Type: application/json
```

```json
{
  "email": "nihad@example.com",
  "password": "securePassword123"
}
```

Successful authentication returns:

```json
{
  "accessToken": "access-token",
  "tokenType": "bearer",
  "user": {
    "id": 1,
    "fullName": "Nihad Memmedzade",
    "email": "nihad@example.com"
  }
}
```

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `POST` | `/auth/register` | Create a user account | No |
| `POST` | `/auth/login` | Log in | No |
| `GET` | `/auth/me` | Get current user | Yes |
| `PUT` | `/auth/me/profile` | Update profile | Yes |
| `PUT` | `/auth/me/password` | Change password | Yes |

### Products

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/products` | Get all products |
| `GET` | `/products/{product_id}` | Get one product |
| `GET` | `/products/filter` | Filter and sort products |
| `GET` | `/products/search` | Search products |
| `GET` | `/products/new-arrivals` | Get new arrivals |
| `GET` | `/products/top-rated` | Get top rated products |
| `GET` | `/products/best-seller` | Get best sellers |
| `GET` | `/products/limited-edition` | Get limited edition products |
| `GET` | `/products/{product_id}/related` | Get related products |

### Reviews

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/products/{product_id}/reviews` | Get product reviews |
| `POST` | `/products/{product_id}/reviews` | Submit a review |

### Wishlist

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/wishlist` | Get user wishlist | Yes |
| `POST` | `/wishlist/{product_id}` | Add product to wishlist | Yes |
| `DELETE` | `/wishlist/{product_id}` | Remove product | Yes |

### Cart

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/cart` | Get user cart | Yes |
| `POST` | `/cart` | Add product to cart | Yes |
| `PUT` | `/cart/{product_id}` | Update product quantity | Yes |
| `DELETE` | `/cart/{product_id}` | Remove cart item | Yes |
| `DELETE` | `/cart` | Clear the cart | Yes |

### Orders

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/orders` | Get user orders | Yes |
| `GET` | `/orders/{order_id}` | Get order details | Yes |
| `POST` | `/orders` | Create an order | Yes |

## Product Filtering

Example:

```text
GET /products/filter?category=Classic%20Cake&flavors=Chocolate&minPrice=20&maxPrice=80&sort=priceLow&lang=en
```

Supported filter parameters:

| Parameter | Description |
|---|---|
| `category` | Product category |
| `flavors` | One or more flavors |
| `tags` | Dietary or product tags |
| `sizes` | One or more sizes |
| `minPrice` | Minimum price |
| `maxPrice` | Maximum price |
| `sort` | Product sorting method |
| `lang` | Product response language |

Supported sorting values:

```text
priceLow
priceHigh
ratingHigh
newest
bestSeller
```

## Product Search

```text
GET /products/search?q=chocolate&lang=en
```

Search checks product titles, categories and flavors in all supported languages.

## Multilingual Product Content

Supported product languages:

| Code | Language |
|---|---|
| `en` | English |
| `az` | Azerbaijani |
| `pl` | Polish |

Examples:

```text
GET /products?lang=en
GET /products?lang=az
GET /products?lang=pl
GET /products/1?lang=az
GET /products/1/related?lang=pl
GET /wishlist?lang=az
GET /cart?lang=pl
GET /orders?lang=en
```

If the selected language is unavailable, the API falls back to English.

Localized product fields include:

- Title
- Category
- Flavor
- Description

## Cart Behaviour

A cart item is identified by:

- User ID
- Product ID
- Selected size

Adding the same product with the same size increases its quantity. Adding the same product with another size creates a separate cart item.

Guest carts are handled by the frontend using local storage. Authenticated user carts are stored permanently in PostgreSQL.

## Wishlist Behaviour

Authenticated wishlists are stored in PostgreSQL. Duplicate products cannot be added because each user and product combination is unique.

Guest wishlists are managed by the frontend using local storage.

## Review Behaviour

A review contains:

- Customer name
- Email address
- Rating from 1 to 5
- Review text
- Creation date

After a review is created, the backend recalculates and updates the product's average rating.

## Order Behaviour

When an order is created, the backend:

1. Validates the authenticated user.
2. Reads products from the submitted items or saved cart.
3. Verifies that every product exists.
4. Uses the current discounted price when available.
5. Calculates the subtotal.
6. Calculates 5% VAT.
7. Creates the order and order items.
8. Clears the authenticated user's cart.
9. Returns the completed order.

Order status starts as:

```text
pending
```

## Validation Rules

Examples of request validation:

- Full name must contain at least 2 characters
- Password must contain at least 6 characters
- Email must have a valid structure
- Cart quantity must be at least 1
- Review rating must be between 1 and 5
- Review text must contain at least 5 characters
- Billing fields are required during checkout

## Common Status Codes

| Code | Meaning |
|---|---|
| `200` | Request completed successfully |
| `201` | Resource created successfully |
| `400` | Invalid operation |
| `401` | Missing, invalid or expired access token |
| `404` | Requested resource was not found |
| `409` | Resource already exists |
| `422` | Request validation failed |
| `500` | Internal server or database error |

## Troubleshooting

### 401 Unauthorized

Make sure the request contains:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Log in again if the token has expired.

### PostgreSQL connection error

Check that:

- PostgreSQL is running
- `DATABASE_URL` is correct
- Database and user exist
- The password is correct
- PostgreSQL is listening on port `5432`

### Permission denied for table

Connect as `postgres` and run:

```sql
\c cake_house_db

GRANT ALL PRIVILEGES
ON ALL TABLES IN SCHEMA public
TO cake_house_user;

GRANT ALL PRIVILEGES
ON ALL SEQUENCES IN SCHEMA public
TO cake_house_user;
```

### 422 Unprocessable Content

Compare the submitted JSON body with the endpoint schema shown in Swagger:

```text
http://127.0.0.1:8000/docs
```

### Frontend receives a CORS error

Add the frontend URL to `ORIGINS`:

```env
ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Restart the backend after changing `.env`.

## Security Notes

- Passwords are never stored as plain text.
- Passwords use salted PBKDF2-HMAC-SHA256 hashes.
- Protected endpoints require bearer authentication.
- Access tokens contain an expiration time.
- Sensitive configuration is loaded from `.env`.
- `.env` must never be committed to GitHub.
- Use a long random `SECRET_KEY` in production.
- Restrict `ORIGINS` to trusted frontend domains in production.

## Production Recommendations

Before deployment:

- Replace the development `SECRET_KEY`
- Set the production PostgreSQL URL
- Restrict allowed CORS origins
- Disable Uvicorn reload mode
- Use HTTPS
- Add Alembic database migrations
- Add automated tests
- Add structured logging
- Use a production ASGI server configuration
- Store secrets in the hosting provider's environment settings

## Frontend Integration

The backend is designed for the Cake House React frontend.

Default local addresses:

```text
Frontend: http://localhost:5173
Backend:  http://127.0.0.1:8000
API Docs: http://127.0.0.1:8000/docs
```

The frontend sends the access token using:

```http
Authorization: Bearer ACCESS_TOKEN
```

Product language is sent through the `lang` query parameter.

## Author

**Nihad Memmedzade**

Cake House was developed as a full-stack university project using React, TypeScript, Redux Toolkit, FastAPI, SQLAlchemy and PostgreSQL.