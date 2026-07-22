# 📘 Assignment: Intro to REST — Simple GET & POST with FastAPI

## 🎯 Objective

Learn the basics of HTTP and JSON by building two minimal FastAPI endpoints: a `GET /hello` and a `POST /echo` that accepts and returns JSON.

## 📝 Tasks

### 🛠️ Create two minimal endpoints

#### Description
Create a FastAPI app that exposes a `GET /hello` endpoint returning a simple greeting and a `POST /echo` endpoint that accepts a JSON payload and returns it back.

#### Requirements

- Implement `GET /hello` that returns `{ "message": "Hello, world!" }`.
- Implement `POST /echo` that accepts a JSON object with a `message` field and returns the same object with a `received` boolean.
- Use Pydantic models for request/response validation.
- Include example `curl` commands to exercise both endpoints.

### 🛠️ Run locally

#### Description
Start the server using Uvicorn and test endpoints with `curl` or a browser.

#### Requirements

- Add `requirements.txt` listing `fastapi` and `uvicorn`.
- Provide the command to run the server: `uvicorn main:app --reload`.

#### Example requests

```
# Start server
uvicorn main:app --reload

# GET hello
curl http://127.0.0.1:8000/hello

# POST echo
curl -X POST http://127.0.0.1:8000/echo -H "Content-Type: application/json" -d '{"message":"Hi"}'
```

Notes: Keep the implementation minimal and beginner-friendly so students can complete it in 10–20 minutes.
