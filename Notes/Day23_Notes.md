# Day 23 Notes

## Backend
- HTTP Request: Request Line, Headers, Blank Line, Body
- HTTP Response: Status Line, Headers, Blank Line, Body
- Content-Type is a header because the server must know how to parse the body before reading it.
- Status Codes:
  - 200 OK
  - 201 Created
  - 400 Bad Request
  - 401 Unauthorized
  - 403 Forbidden
  - 404 Not Found
  - 500 Internal Server Error

## FastAPI
- Created and activated a virtual environment.
- Installed FastAPI and Uvicorn.
- Built first API.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Backend Engineer!"}
```

Run:
```bash
uvicorn main:app --reload
```

## DSA
- Built Prefix Sum array.
- Formula:
  - L == 0 -> prefix[R]
  - Else -> prefix[R] - prefix[L-1]

Complexities:
- Build: O(N)
- Query: O(1)

## Homework
- Create /about endpoint.
- Observe 404 on unknown route.
- Solve LeetCode 1480 and 303.
