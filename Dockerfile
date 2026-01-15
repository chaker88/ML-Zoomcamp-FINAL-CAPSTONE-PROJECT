# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies needed for TensorFlow and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project
COPY . /app/

# Install Python dependencies using pip
RUN pip install --no-cache-dir \
    fastapi>=0.128.0 \
    uvicorn>=0.40.0 \
    tensorflow>=2.20.0 \
    numpy>=2.4.0 \
    pydantic>=2.0 \
    joblib

# Expose port 8000
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
