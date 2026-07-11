import numpy as np
from sklearn.linear_model import LinearRegression
from sqlalchemy.orm import Session
from ...domains.sales.models import Order
from ...domains.operations.models import SKU


def calculate_ma(history: list, window: int = 3) -> float:
    if len(history) < window:
        return float(np.mean(history)) if history else 0.0
    return float(np.mean(history[-window:]))


def calculate_wma(history: list, window: int = 3) -> float:
    if len(history) < window:
        return calculate_ma(history, window)
    weights = np.arange(1, window + 1)
    return float(np.dot(history[-window:], weights) / weights.sum())


def calculate_es(history: list, alpha: float = 0.3) -> float:
    if not history:
        return 0.0
    val = history[0]
    for x in history[1:]:
        val = alpha * x + (1 - alpha) * val
    return float(val)


def calculate_lr(history: list, steps_ahead: int = 1) -> float:
    if len(history) < 2:
        return history[-1] if history else 0.0
    X = np.arange(len(history)).reshape(-1, 1)
    y = np.array(history)
    model = LinearRegression().fit(X, y)
    next_t = np.array([[len(history) + steps_ahead - 1]])
    return float(model.predict(next_t)[0])


def forecast_demand(db: Session, sku_id: int, model_name: str = "MA", period_days: int = 30):
    history = [120, 135, 110, 145, 160, 150, 175, 190]
    predictions = []
    current_history = list(history)

    for i in range(1, period_days + 1):
        if model_name == "MA":
            val = calculate_ma(current_history)
        elif model_name == "WMA":
            val = calculate_wma(current_history)
        elif model_name == "ES":
            val = calculate_es(current_history)
        elif model_name == "LR":
            val = calculate_lr(current_history, steps_ahead=i)
        else:
            val = calculate_ma(current_history)

        predictions.append(round(val, 2))
        current_history.append(val)

    return {
        "sku_id": sku_id,
        "model": model_name,
        "period_days": period_days,
        "historical": history,
        "forecast": predictions
    }


def forecast_sales(db: Session, period_days: int = 30):
    history = [12000, 13500, 14000, 13800, 15500, 16000]
    predictions = []
    current_history = list(history)
    for i in range(period_days):
        val = calculate_lr(current_history, steps_ahead=i + 1)
        predictions.append(round(val, 2))
        current_history.append(val)
    return {"historical": history, "forecast": predictions}


def predict_revenue(db: Session, period_days: int = 90):
    return forecast_sales(db, period_days)


def predict_expenses(db: Session, period_days: int = 90):
    history = [8000, 8500, 9000, 9200, 9500, 9800]
    predictions = []
    current_history = list(history)
    for i in range(period_days):
        val = calculate_ma(current_history)
        predictions.append(round(val, 2))
        current_history.append(val)
    return {"historical": history, "forecast": predictions}
