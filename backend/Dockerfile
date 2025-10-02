# backend/Dockerfile
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set workdir
WORKDIR /app

# Copy pyproject + lock
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root --without dev

# Copy app
COPY app ./app

# Run server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
