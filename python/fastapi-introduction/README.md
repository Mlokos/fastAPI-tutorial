# Run server:
poetry run uvicorn example1:app --reload

# Web pages to visit after server startup:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/items/5?q=somequery
- http://127.0.0.1:8000/docs
- [optional] http://127.0.0.1:8000/redoc