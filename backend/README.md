# Backend Docker Setup

This directory contains the FastAPI backend for the furniture recommendation system.

## Running with Docker

### Prerequisites
- Docker and Docker Compose installed and running

### Quick Start
```bash
# From the project root directory
docker-compose up --build -d
```

### Manual Docker Commands
```bash
# Build the Docker image
docker build -t furniture-backend ./backend

# Run the container
docker run -p 7600:7600 -v $(pwd)/backend:/app furniture-backend
```

### API Endpoints
Once running, the API will be available at:
- Health check: http://localhost:7600/
- Recommendations: http://localhost:7600/recommend?query=chair
- Category prediction: http://localhost:7600/predict-category?image_path=image_url
- Description generation: http://localhost:7600/generate-description?prompt=creative_description

### Development
To run locally without Docker:
```bash
pip install -r requirements.txt
python main.py
```

The application will run on port 7600.
