# Task 2 — PEP 8 Code Cleanup

## Overview

This task refactors messy Python code according to PEP 8 and improves its readability.

## PEP 8 Changes

Added 4-space indentation.
Added spaces after commas and around operators.
Changed `userName` to `user_name` using snake_case.
Added blank lines between logical sections.
Used a meaningful variable name, `result`, instead of `x`.
Improved the overall readability and consistency of the code.

## Tools

The code can optionally be checked using Ruff or formatted using Black.

```bash
ruff check main.py
black main.py
```

Ruff checks for code quality and style issues, while Black automatically formats the code.

## What I Learned

I learned that PEP 8 provides guidelines for writing clean, readable, and consistent Python code. I also learned how Ruff and Black can help identify and automatically fix formatting and style issues.

# Task 3 — Data Validation in Flask and FastAPI

## Overview

This task compares data validation in **Flask** and **FastAPI** using a `POST /predict` endpoint with a required `text` field.

No machine learning model is used. The endpoint returns a fixed sentiment response.

## How to Run

### Flask

```bash
python flaskapi.py
```

### FastAPI

```bash
uvicorn fast:app --reload
```

## Example Request

```json
{"text": "I love this product"}
```

## Valid Response

```json
{"sentiment": "positive"}
```

## Validation Tests

Both APIs were tested with:

Valid JSON
Missing `text`
Empty string
Non-string value


Flask performs validation manually using request data, while FastAPI uses a Pydantic model and type hints to automatically validate the request.

## Comparison

Flask:More manual validation code is required, and error responses are created explicitly.

FastAPI: Validation is declared in the Pydantic model, and FastAPI automatically returns structured `422` validation errors.

## What I Learned

I learned that Flask commonly uses explicit validation, while FastAPI uses type hints and Pydantic to automatically parse and validate request data.
