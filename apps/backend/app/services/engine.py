from sqlalchemy.orm import Session
from app.models.sales import SalesOrder
import numpy as np

def run_baseline_forecast(sku: str, db: Session):
    """
    Lightweight processing engine.
    Safely calculates moving average trends without triggering high memory usage 
    or Out-Of-Memory (OOM) failures on the Render free tier.
    """
    sales_history = db.query(SalesOrder).filter(SalesOrder.product_sku == sku).all()
    
    if len(sales_history) < 3:
        # Fallback metric if history points are low
        return [15, 18, 20] 
        
    quantities = [order.quantity for order in sales_history]
    moving_avg = float(np.mean(quantities[-3:]))
    
    # Generate mock progressive data based on historical moving values
    return [round(moving_avg * 1.05, 1), round(moving_avg * 1.1, 1), round(moving_avg * 1.15, 1)]