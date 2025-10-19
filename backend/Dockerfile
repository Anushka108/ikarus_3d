# Use Python 3.9 slim image for smaller size
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies for PyTorch and other ML libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory
COPY . .

# Expose port 7500
EXPOSE 7500

# Run the FastAPI application
CMD ["python", "main.py"]
