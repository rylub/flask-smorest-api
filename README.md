# Flask Smorest API

A RESTful API built with Flask-Smorest, SQLAlchemy, and JWT authentication.  
This project includes CRUD operations for stores, items, tags, and users.  
It is containerized with Docker and uses Flask-Migrate for database version control.

---

## Technical Stack

**Languages:** Python 3.13  
**Frameworks & Libraries:** Flask, Flask-Smorest, SQLAlchemy, Marshmallow, Flask-Migrate, Flask-JWT-Extended  
**Database:** SQLite (default), compatible with PostgreSQL or MySQL  
**Containerization:** Docker  
**API Documentation:** Swagger UI (OpenAPI 3.0.3)  
**Environment:** Windows development environment with virtualenv  
**Version Control:** Git and GitHub  

---

## Features

- Flask-Smorest blueprint-based API architecture  
- JWT authentication and token revocation  
- CRUD endpoints for users, stores, items, and tags  
- SQLAlchemy ORM integration  
- Flask-Migrate for schema migrations  
- Swagger UI for API documentation  
- Docker support for consistent local development  
- SQLite database (default, configurable for production)

---

## Project Structure

Rest_API_Project/  
├── app/  
│   ├── models/                # SQLAlchemy models  
│   ├── resources/             # Flask-Smorest route handlers  
│   ├── schemas.py             # Marshmallow schemas  
│   ├── db.py                  # Database initialization  
│   ├── app.py                 # Application factory  
│   ├── blocklist.py           # JWT blocklist  
│   └── __init__.py  
├── migrations/                # Alembic migration scripts  
├── instance/                  # Local database  
├── Dockerfile  
├── requirements.txt  
└── README.md  

---

## Getting Started

### 1. Clone the repository
```
git clone https://github.com/rylub/flask-smorest-api.git
cd flask-smorest-api
```

### 2. Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the application locally
```
flask run
```

**Local API URL:**  
http://127.0.0.1:5000  

**Swagger documentation:**  
http://127.0.0.1:5000/swagger-ui  

---

## Running with Docker

### Build the image
```
docker build -t flask-smorest-api .
```

### Run the container (Windows)
```
docker run -dp 5005:5000 --name flask-smorest-api -w /app -v "%cd%:/app" -e FLASK_ENV=development -e FLASK_DEBUG=1 flask-smorest-api
```

**API available at:**  
http://127.0.0.1:5005/swagger-ui  

---

## Database Migrations

To create or update database schema changes:
```
flask db migrate -m "description of changes"
flask db upgrade
```

---

## API Endpoints Overview

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /register | Register a new user |
| POST | /login | Authenticate a user and return JWT |
| POST | /logout | Revoke access token |
| POST | /store | Create a new store |
| GET | /store/<id> | Get store by ID |
| POST | /item | Create a new item |
| GET | /item/<id> | Get item by ID |
| POST | /tag | Create a tag |
| GET | /tag/<id> | Get tag by ID |

For complete interactive documentation, visit the Swagger UI.

---

## License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it as long as proper attribution is provided.

---

**Author:** Ryan Lubell  
[LinkedIn Profile](https://www.linkedin.com/in/ryanlubell)
