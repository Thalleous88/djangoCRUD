# Product API – Backend Intern Challenge

## Overview

This project is a simple RESTful API built to help retailers record and manage their products. It allows users to create, retrieve, update, and delete products via HTTP endpoints. No frontend is included, but API documentation is provided.

The application is implemented using **Django** and **Django REST Framework (DRF)**.

---

## Tech Stack

* **Python 3.10.11**
* **Django 5.2.9**
* **Django REST Framework**
* **PostgreSQL** 
* **drf-spectacular** (OpenAPI / Swagger / ReDoc documentation)

We use Django because of my familiarity with Python, its rich set of built-in features, and its suitability for the challenge requirements. Django REST Framework (DRF) is chosen as it provides robust abstractions for common CRUD patterns and handles much of the repetitive logic such as HTTP method routing, serialization (JSON → Python objects → database), validation, standardized API responses, pagination, and more. DRF also integrates well with API documentation tools like drf-spectacular, enabling automatic OpenAPI/Swagger documentation.

Finally, PostgreSQL is used as the database because it is fast, reliable, and works seamlessly with Django. It supports high concurrency through Multi-Version Concurrency Control (MVCC), allowing multiple users to read and write data simultaneously without compromising data integrity.

---

## Core Requirements Addressed

* Create a product (POST)
* Retrieve an existing product (GET)
* Update a product (PUT/PATCH)
* Delete a product (DELETE)
* Support **arbitrary product fields** using JSONField

Example request body:

```json
{
  "fields": {
    "name": "Ultramie Goreng",
    "price": 25000
  }
}
```

Example response:

```json
{
  "id": 1,
  "fields": {
    "name": "Ultramie Goreng",
    "price": 25000
  }
}
```

---

## Data Model Design

### Why JSON Fields?

Products are designed to support **arbitrary attributes** (e.g. name, price, stock, category). Instead of enforcing a rigid relational schema, product attributes are stored in a JSON field as instructed in the requirement.

---

## API Design

### Endpoints

| Method      | Endpoint          | Description          |
| ----------- | ----------------- | -------------------- |
| GET         | `/products/`      | List all products    |
| POST        | `/products/`      | Create a new product |
| GET         | `/products/{id}/` | Retrieve a product   |
| PUT / PATCH | `/products/{id}/` | Update a product     |
| DELETE      | `/products/{id}/` | Delete a product     |

---

## Design Decision: Merge-Based Updates

### Problem

As required in the challenge, **that the system will only overwrite only the fields included in that payload**, so we will overwrite the update function (PATCH & PUT) from the standard Generic API View.

---

### Chosen Approach

When updating a product, the API **merges the incoming fields into the existing JSON object** instead of replacing it entirely.

#### Example

Existing product:

```json
{
  "fields": {
    "name": "Ultramie Goreng",
    "price": 25000,
    "stock": 10
  }
}
```

Update request:

```json
{
  "fields": {
    "price": 27000
  }
}
```

Result:

```json
{
  "fields": {
    "name": "Ultramie Goreng",
    "price": 27000,
    "stock": 10
  }
}
```

Only the provided keys are updated; all other fields remain unchanged.

---

### REST Semantics

Although standard REST conventions treat `PUT` as a full replacement, this API intentionally treats updates as **merge-based operations**. This behavior is explicitly documented in the API schema to avoid ambiguity.

---

### Validation

To ensure predictable behavior:

* The `fields` attribute **must exist** in update requests
* The `fields` attribute **must be a JSON object**

Invalid payloads return a `400 Bad Request` response with a clear error message.

---

## API Documentation

The API is documented using an **OpenAPI schema**, automatically generated from the codebase.

Available documentation:

* **Swagger UI** – interactive testing
* **ReDoc** – clean, readable documentation


---

## Running the Project

1. Create a virtual environment
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Configure the database in `settings.py`
4. Run migrations

   ```bash
   python manage.py migrate
   ```
5. Start the development server

   ```bash
   python manage.py runserver
   ```

---

