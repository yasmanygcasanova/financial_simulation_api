from typing import Any, Dict, List

import numpy as np


def get_seasonality(user_input: str = None) -> List[float]:
    if user_input is None or user_input.strip() == "":
        return np.random.uniform(-0.2, 0.2, 12).tolist()
    try:
        seasonality = [float(s) for s in user_input.split(",")]
        if len(seasonality) != 12:
            raise ValueError("Exactly 12 values are required.")
        return seasonality
    except ValueError:
        return np.random.uniform(-0.2, 0.2, 12).tolist()


def calculate_monthly_results(
    month: int, base_sales: float, seasonality: List[float], config: Dict[str, Any]
) -> Dict[str, float]:
    seasonal_factor = 1 + seasonality[month - 1]
    adjusted_sales = base_sales * seasonal_factor

    supply_cost = adjusted_sales * config["SUPPLY_COST"]
    packaging_cost = adjusted_sales * config["PACKAGING_COST"]
    delivery_costs = adjusted_sales * config["DELIVERY_FEES"]
    variable_costs = supply_cost + packaging_cost
    royalties = adjusted_sales * config["ROYALTY_PERCENTAGE"]
    national_marketing = adjusted_sales * config["NATIONAL_MARKETING_PERCENTAGE"]
    taxes = adjusted_sales * config["TAX_PERCENTAGE"]

    net_profit = adjusted_sales - (
        config["FIXED_COSTS"]
        + variable_costs
        + royalties
        + national_marketing
        + delivery_costs
        + taxes
        + config["LOCAL_MARKETING_COST"]
    )

    return {
        "month": month,
        "adjusted_sales": round(adjusted_sales, 2),
        "royalties": round(royalties, 2),
        "national_marketing": round(national_marketing, 2),
        "fixed_costs": round(config["FIXED_COSTS"], 2),
        "variable_costs": round(variable_costs, 2),
        "delivery_costs": round(delivery_costs, 2),
        "taxes": round(taxes, 2),
        "local_marketing": round(config["LOCAL_MARKETING_COST"], 2),
        "net_profit": round(net_profit, 2),
    }


def calculate_growth_adjusted_sales(
    base_sales: float, growth_rate: float, month: int
) -> float:
    adjusted_sales = base_sales * (1 + growth_rate) ** (month / 12)

    # Check if the result is a complex number
    if isinstance(adjusted_sales, complex):
        # Round the real and imaginary parts separately
        real_part = round(adjusted_sales.real, 2)
        imag_part = round(adjusted_sales.imag, 2)
        return complex(real_part, imag_part)  # Return a rounded complex number

    return round(adjusted_sales, 2)  # Normally round if it's a real number


def calculate_contribution_margin(
    adjusted_sales: float, variable_costs: float
) -> float:
    return adjusted_sales - variable_costs


def calculate_break_even_point(
    fixed_costs: float, contribution_margin_ratio: float
) -> float:
    return fixed_costs / contribution_margin_ratio


def calculate_roi(net_profit: float, initial_investment: float) -> float:
    if initial_investment > 0:
        roi = (net_profit / initial_investment) * 100
        return round(roi, 2)
    return 0.0
