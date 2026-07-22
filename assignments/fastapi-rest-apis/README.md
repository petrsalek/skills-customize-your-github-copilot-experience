# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework. Students will learn to define routes, use Pydantic models for request/response validation, handle path/query parameters, and run the app locally for manual testing.

## 📝 Tasks

### 🛠️ Create core endpoints

#### Description
Implement the basic API routes: a `GET` list endpoint and a `POST` endpoint that accepts a JSON payload validated with a Pydantic model.

#### Requirements

- Create a FastAPI app in `main.py` exposing at least two endpoints: `GET /items` and `POST /items`.
- Use a Pydantic model for the `POST` request body and return the created item in the response.

### 🛠️ Add parameters and validation

#### Description
Add path and query parameters with validation to filter or fetch individual resources.

#### Requirements

- Add a `GET /items/{item_id}` endpoint that returns a single item by `item_id`.
- Support a query parameter for pagination or filtering (e.g., `?limit=10`).
- Validate parameter types and return `400` for invalid input.

### 🛠️ (Optional) Testing and running locally

#### Description
Run the app locally and (optionally) write simple tests using FastAPI's TestClient.

#### Requirements

- Start the app with Uvicorn and verify endpoints with `curl` or a browser.
- (Optional) Add a basic test using `fastapi.testclient.TestClient` that checks the `GET /items` response.

#### Example requests

```
# Run server
uvicorn main:app --reload

# List items
curl http://127.0.0.1:8000/items

# Create item
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name": "Notebook", "price": 12.5}'
```

**Notes:** Include clear, minimal code in `main.py` so instructors can run and review the solution easily. Add `requirements.txt` with `fastapi` and `uvicorn` for convenience.
