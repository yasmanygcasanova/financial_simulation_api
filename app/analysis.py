from typing import Dict, List

from .simulation import (
    calculate_break_even_point,
    calculate_contribution_margin,
    calculate_roi,
)


def perform_financial_analysis(results: List[Dict], initial_investment: float) -> Dict:
    total_sales = sum(r["adjusted_sales"] for r in results)
    total_variable_costs = sum(r["variable_costs"] for r in results)
    total_fixed_costs = sum(r["fixed_costs"] for r in results)
    total_net_profit = sum(r["net_profit"] for r in results)

    contribution_margin = calculate_contribution_margin(
        total_sales, total_variable_costs
    )
    contribution_margin_ratio = contribution_margin / total_sales

    break_even_point = calculate_break_even_point(
        total_fixed_costs, contribution_margin_ratio
    )
    roi = calculate_roi(total_net_profit, initial_investment)

    return {
        "break_even_point": break_even_point,
        "roi": roi,
        "contribution_margin": contribution_margin,
        "contribution_margin_ratio": contribution_margin_ratio,
    }


def calculate_monthly_growth_rate(results: List[Dict]) -> float:
    sales = [r["adjusted_sales"] for r in results]
    return (sales[-1] / sales[0]) ** (
        1 / 11
    ) - 1  # Because there are 12 months, but 11 intervals
