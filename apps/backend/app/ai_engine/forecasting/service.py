"""Forecasting service stubs: Sales & Demand Time-Series, Revenue/Expense prediction."""


def forecast_sales(period_days: int = 30):
    """Generate sales forecast for the given period."""
    pass


def forecast_demand(sku_id: int, period_days: int = 30):
    """Generate demand forecast for a specific SKU."""
    pass


def predict_revenue(period_days: int = 90):
    """Predict revenue trend lines for 30/60/90-day windows."""
    pass


def predict_expenses(period_days: int = 90):
    """Predict expense trend lines for 30/60/90-day windows."""
    pass
