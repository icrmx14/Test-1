from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .forecasting import service as forecast_service

router = APIRouter()


@router.get("/forecast/demand/{sku_id}")
def get_demand_forecast(sku_id: int, model: str = "MA", period: int = 30, db: Session = Depends(get_db)):
    return forecast_service.forecast_demand(db, sku_id, model, period)


@router.get("/forecast/sales")
def get_sales_forecast(period: int = 30, db: Session = Depends(get_db)):
    return forecast_service.forecast_sales(db, period)


@router.get("/forecast/revenue")
def get_revenue_forecast(period: int = 90, db: Session = Depends(get_db)):
    return forecast_service.predict_revenue(db, period)


@router.get("/forecast/expenses")
def get_expenses_forecast(period: int = 90, db: Session = Depends(get_db)):
    return forecast_service.predict_expenses(db, period)


@router.get("/anomalies/expenses")
def get_expense_anomalies():
    return {"anomalies": []}


@router.post("/copilot/chat")
def copilot_chat(message: str):
    # Standard handler helper stub
    return {"reply": f"ERP Copilot response for: '{message}'"}
