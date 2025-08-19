# Compliance Report API

A FastAPI service that generates compliance assessment reports with detailed section analysis.

## Features

- RESTful API for compliance report generation
- Structured responses with Pydantic models
- Health check endpoints
- Docker containerization
- Automatic API documentation

## API Endpoints

- `GET /` - API information  
- `GET /api/v1/report` - Generate compliance report  
- `GET /health` - Health check  
- `GET /docs` - Interactive API documentation  

## Local Development

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone or create the project folder:**
```bash
mkdir compliance-report-api
cd compliance-report-api
````

2. **Create and activate a virtual environment:**

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
# Development mode with auto-reload
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

5. **Access the application:**

* API: [http://localhost:8000/api/v1/report](http://localhost:8000/api/v1/report)
* Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* Health: [http://localhost:8000/health](http://localhost:8000/health)

6. **Deactivate virtual environment**

```bash
deactivate
```

## Docker Deployment

### Build and Run

```bash
docker build -t compliance-report-api .
docker run -d -p 8000:8000 --name compliance-api compliance-report-api
```

### Docker Commands

```bash
docker stop compliance-api
docker start compliance-api
docker rm compliance-api
docker logs compliance-api
docker ps
```

## Project Structure

```
compliance-report-api/
├── src/
│   ├── models/
│   │   └── schemas.py
│   ├── data/
│   │   └── sample_report.py
│   └── main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## License

MIT License