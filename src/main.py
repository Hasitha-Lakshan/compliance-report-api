from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.data.sample_report import get_sample_report
from src.models.schemas import ReportResponse

app = FastAPI(
    title="Compliance Report API",
    description="API for generating compliance assessment reports with detailed section analysis",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

@app.get("/")
async def root():
    return {
        "message": "Compliance Report API",
        "version": "1.0.0",
        "endpoints": {
            "report": "/api/v1/report",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.get("/api/v1/report", response_model=ReportResponse)
async def generate_compliance_report():
    """
    Generate a compliance assessment report with detailed section analysis.
    
    Returns a comprehensive report including:
    - Overall status and report ID
    - PDF download URL
    - Multiple sections with sub-domain analysis
    - Question-level results with relevance scores
    - Reference documentation
    """
    return get_sample_report()

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring and readiness probes"""
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "compliance-report-api",
            "version": "1.0.0"
        }
    )

@app.get("/api/v1/report/health")
async def report_service_health():
    """Health check specifically for the report generation service"""
    return {
        "status": "operational",
        "component": "report-generator",
        "message": "Report generation service is healthy"
    }