from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.engine import run_baseline_forecast

router = APIRouter(prefix="/forecasting", tags=["AI Forecasting Core"])

@router.get("/predict/{sku}")
def get_product_forecast(sku: str, db: Session = Depends(get_db)):
    # Pulls execution values down from the lightweight mathematical engine layer
    predictions = run_baseline_forecast(sku, db)
    return {
        "sku": sku,
        "forecast_method": "Exponential Smoothing / Historical Moving Average",
        "monthly_predictions": predictions
    }