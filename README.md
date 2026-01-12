# Ecommerce Data Pipeline (Python ETL)

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-enabled-cyan)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
This repository contains a modular **ETL (Extract, Transform, Load)** pipeline designed to automate data ingestion for e-commerce platforms. The system is built to handle supplier data from JSON sources, apply business-logic validation, and persist clean data into a relational SQL database.

The project reflects my transition from direct e-commerce management to **Software Engineering**, applying professional patterns to real-world business problems.

## 🛠️ Technical Architecture & Patterns
To ensure scalability and maintainability, the project follows several key engineering principles:

* **Separation of Concerns (SoC)**: Logic is split into dedicated modules for Database management, ETL logic, and Utility decorators.
* **Decorator Pattern**: Implemented custom Python decorators for automated logging and execution monitoring, keeping the business logic clean and "DRY" (Don't Repeat Yourself).
* **Data Integrity Layer**: A transformation step filters out invalid entries (e.g., negative pricing or missing mandatory fields) before database ingestion.
* **Containerization**: Fully Dockerized to ensure environment parity across development and production.

## 📂 Project Structure
```text
.
├── main.py              # Application Entry Point
├── Dockerfile           # Container configuration
├── requirements.txt     # Dependency management
├── data/                # Raw input data (JSON/CSV)
└── src/                 # Core logic
    ├── database.py      # SQLite connection & ORM-like logic
    ├── pipeline.py      # ETL process (Extract-Transform-Load)
    └── decorators.py    # Custom functional wrappers
