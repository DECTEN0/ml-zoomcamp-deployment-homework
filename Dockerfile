# Use the official uv base image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

# Set working directory
WORKDIR /app

# Copy only dependency files first (for layer caching)
COPY deployment/pyproject.toml deployment/uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy app code
COPY deployment .

# Run FastAPI with uvicorn
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
