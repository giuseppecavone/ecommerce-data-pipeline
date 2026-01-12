# 🛒 Professional Ecommerce Data Pipeline & REST API

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![JWT](https://img.shields.io/badge/Auth-JWT-black?logo=json-web-tokens)](https://jwt.io/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)](https://www.sqlite.org/)

## 📌 Project Overview
This is a high-performance, modular backend system for an E-commerce platform. It integrates a **Python ETL Pipeline** with a **RESTful API** layer, featuring secure user authentication and transactional order management.

Designed with **enterprise-grade patterns**, this project demonstrates the transition from raw data processing to a scalable, secure web architecture.

## 🚀 Key Features & Engineering Patterns

### 🔐 Advanced Security & Auth
- **JWT (JSON Web Tokens)**: Stateless authentication implemented via custom Python decorators for protected routes.
- **Security First**: Password hashing using **SHA-256** to ensure data protection at rest.
- **Role-Based Access**: Separation between public endpoints (Product Catalog) and protected transactional endpoints (Checkout).

### 🏛️ Modular Architecture (Service Layer Pattern)
To ensure the **Single Responsibility Principle**, the logic is decoupled into:
- **API Routes**: Handling HTTP requests/responses using Flask Blueprints.
- **Service Layer**: Business logic isolation (Validation, Hashing, Formatting).
- **Data Access Layer**: Relational mapping and persistence with SQLite.

### 🛠️ Robustness & DevOps
- **Centralized Error Handling**: Custom exception mapping to standardized JSON responses.
- **Data Validation**: Strict integrity checks on prices, user inputs, and relational foreign keys.
- **Containerization**: Fully Dockerized for environment consistency.

## 📂 Project Structure
```text
.
├── app.py              # Server Entry Point & Global Config
├── src/
│   ├── api_routes.py    # Modular API Endpoints (Blueprints)
│   ├── auth.py          # JWT Middleware & Decorators
│   ├── database.py      # Relational DB Schema & Logic
│   ├── services.py      # Product Domain Logic
│   ├── user_service.py   # Auth & User Domain Logic
│   ├── order_service.py  # Transactional Order Logic
│   ├── exceptions.py    # Custom Exception Classes
│   └── decorators.py    # Execution & Logging Wrappers
└── Dockerfile           # Deployment Configuration