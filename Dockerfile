# Use Python 3.12 as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create data directory for outputs
RUN mkdir -p data

# Set Python path
ENV PYTHONPATH=/app

# Default command - run phi convergence simulation
CMD ["python", "simulations/phi_convergence.py"]

# For interactive use:
# docker run -it --rm -v $(pwd)/data:/app/data pqrg-theory bash