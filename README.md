# Employment Prediction API - ML Zoomcamp Capstone Project

## Overview

This project predicts employment status based on developer profile features using a neural network model. The model is deployed as a FastAPI REST API that can be run locally or in a Docker container.

## Problem Statement

Given developer characteristics such as years of coding experience, programming languages known, computer skills, previous salary, and education level, predict whether a developer is currently employed or not.

## Dataset

- **Source**: Stack Overflow Developer Survey data
- **Size**: ~25,000 records (after preprocessing)
- **Features**: 23 features including employment status, salary history, technical skills, and demographics
- **Target**: Binary classification (Employed/Not Employed)

## Project Structure

```
.
├── EDA.ipynb                           # Exploratory Data Analysis notebook
├── ModelBuildNotebook.ipynb            # Model development and training
├── README.md                           # This file
├── Dockerfile                          # Docker configuration
├── .dockerignore                       # Docker ignore file
├── pyproject.toml                      # Python project configuration
├── dataset/
│   ├── stackoverflow_full.csv          # Raw dataset
│   └── stackoverflow_prepared.csv      # Preprocessed dataset
└── app/
    ├── main.py                         # FastAPI application
    ├── schema.py                       # Pydantic models for API validation
    ├── best_model_nn.keras            # Trained neural network model
    └── scaler.joblib                  # Feature scaler (StandardScaler)
```

## Model Details

- **Algorithm**: Neural Network (Sequential model)
- **Framework**: TensorFlow/Keras
- **Architecture**: Deep neural network with multiple layers
- **Training Data**: Preprocessed Stack Overflow survey responses
- **Performance**: Validated on test set with binary classification metrics

## Installation

### Prerequisites
- Python 3.12+
- Docker (optional, for containerized deployment)

### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ML-Zoomcamp\ Capstone
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or using uv
uv sync
```

3. Run the FastAPI server:
```bash
cd app
uv run python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Docker Setup

1. Build the Docker image:
```bash
docker build -t employment-prediction-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 employment-prediction-api
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
**GET** `/`

Returns welcome message and API version.

```bash
curl http://localhost:8000/
```

**Response:**
```json
{
  "message": "Employment Prediction API is running",
  "version": "1.0.0"
}
```

### 2. Health Check
**GET** `/health`

Returns API health status.

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

### 3. Prediction Endpoint
**POST** `/predict`

Makes employment prediction based on input features.

**Request Body:**
```json
{
  "Employment": 1,
  "PreviousSalary": 50000.0,
  "YearsCode": 7,
  "ComputerSkills": 4,
  "Lang_AWS": 0,
  "Lang_Bash/Shell": 1,
  "Lang_C#": 0,
  "Lang_Docker": 0,
  "Lang_Git": 1,
  "Lang_HTML/CSS": 0,
  "Lang_Java": 0,
  "Lang_JavaScript": 0,
  "Lang_Microsoft SQL Server": 0,
  "Lang_MySQL": 0,
  "Lang_Node.js": 1,
  "Lang_Other": 1,
  "Lang_PostgreSQL": 0,
  "Lang_Python": 1,
  "Lang_React.js": 0,
  "Lang_SQL": 1,
  "Lang_TypeScript": 0,
  "Age (>35)": 1,
  "edlevel_encoded": 4
}
```

**Response:**
```json
{
  "prediction": 1,
  "probability": 0.87,
  "interpretation": "Employed"
}
```

## Features

- **23 Input Features**:
  - Employment status (binary)
  - Previous salary (continuous)
  - Years of coding experience (continuous)
  - Computer skills rating (continuous)
  - Programming language skills (21 binary features: AWS, Bash, C#, Docker, Git, HTML/CSS, Java, JavaScript, SQL Server, MySQL, Node.js, Other, PostgreSQL, Python, React.js, SQL, TypeScript)
  - Age group indicator (>35 years)
  - Education level (encoded)

- **Output**:
  - Prediction: 0 (Not Employed) or 1 (Employed)
  - Probability: Confidence score (0.0 to 1.0)
  - Interpretation: Human-readable label

## Technologies Used

- **Backend**: FastAPI
- **ML Framework**: TensorFlow/Keras
- **Data Processing**: NumPy, Scikit-learn, Pandas
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Server**: Uvicorn
- **Containerization**: Docker
- **API Validation**: Pydantic

## Files Description

- **EDA.ipynb**: Exploratory data analysis with visualizations
- **ModelBuildNotebook.ipynb**: Data preprocessing, model architecture, training, and evaluation
- **main.py**: FastAPI application with endpoints
- **schema.py**: Pydantic models for request/response validation
- **best_model_nn.keras**: Pre-trained neural network model
- **scaler.joblib**: Fitted StandardScaler for feature normalization

## Usage Example

### Using cURL:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Employment": 1,
    "PreviousSalary": 75000,
    "YearsCode": 10,
    "ComputerSkills": 5,
    "Lang_AWS": 1,
    "Lang_Bash/Shell": 1,
    "Lang_C#": 0,
    "Lang_Docker": 1,
    "Lang_Git": 1,
    "Lang_HTML/CSS": 0,
    "Lang_Java": 1,
    "Lang_JavaScript": 1,
    "Lang_Microsoft SQL Server": 0,
    "Lang_MySQL": 1,
    "Lang_Node.js": 1,
    "Lang_Other": 0,
    "Lang_PostgreSQL": 1,
    "Lang_Python": 1,
    "Lang_React.js": 1,
    "Lang_SQL": 1,
    "Lang_TypeScript": 1,
    "Age (>35)": 1,
    "edlevel_encoded": 4
  }'
```

### Using Python:
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "Employment": 1,
    "PreviousSalary": 75000,
    "YearsCode": 10,
    "ComputerSkills": 5,
    # ... add other features
}

response = requests.post(url, json=data)
print(response.json())
```

## Interactive API Documentation

When the server is running, access the interactive Swagger UI documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Deployment

### Docker Deployment

1. Build and tag the image:
```bash
docker build -t employment-prediction-api:latest .
```

2. Run with resource limits:
```bash
docker run -p 8000:8000 \
  --memory="2g" \
  --cpus="1" \
  employment-prediction-api:latest
```

3. Push to Docker registry (e.g., Docker Hub):
```bash
docker tag employment-prediction-api:latest <your-username>/employment-prediction-api:latest
docker push <your-username>/employment-prediction-api:latest
```

## Performance Considerations

- Model inference time: ~50-100ms per prediction
- API response time: ~100-150ms per request
- Memory usage: ~500MB-1GB (including TensorFlow)
- CPU: Minimal (can run on CPU-only systems)

## Notes

- The model was trained on Stack Overflow survey data
- All features are required for predictions
- Features are automatically scaled using the trained scaler
- The API includes error handling for invalid inputs

## Author

ML Zoomcamp Capstone Project - 2026

## License

MIT
