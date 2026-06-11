# Building REST APIs with FastAPI

## Overview

In this assignment you'll learn to build a small RESTful API using the FastAPI framework. You'll create endpoints, validate input with Pydantic models, and run the app locally using Uvicorn.

## Learning Objectives

- Understand FastAPI app structure and routing
- Create request and response models with Pydantic
- Implement CRUD-style endpoints
- Run and test the API locally with Uvicorn and curl

## Tasks

1. Explore the starter code in `starter-code.py` and run the app.
2. Implement the following endpoints:
   - `GET /` — returns a welcome message
   - `GET /items/` — list all items
   - `GET /items/{item_id}` — retrieve item by id
   - `POST /items/` — create a new item (validate input)
   - `PUT /items/{item_id}` — update an existing item
   - `DELETE /items/{item_id}` — delete an item
3. Add input validation and appropriate HTTP status codes.
4. Provide example `curl` commands in your README demonstrating each endpoint.

## Setup

1. Create a virtual environment and install dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```
uvicorn starter-code:app --reload
```

The app will run on `http://127.0.0.1:8000` by default.

## Deliverables

- Completed endpoints in `starter-code.py`
- A short usage section with `curl` examples in this README

## Grading Rubric

- Functionality: 60% — endpoints behave as specified
- Validation & error handling: 20% — proper status codes and checks
- Documentation: 10% — clear run and usage instructions
- Code style & readability: 10% — clean, idiomatic Python

## Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Pydantic docs: https://pydantic-docs.helpmanual.io/
