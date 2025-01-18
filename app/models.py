from typing import List

from pydantic import BaseModel, Field, field_validator


class SimulationInput(BaseModel):
    seasonality: List[float] = Field(
        default=[0.1, -0.05, 0.02, 0.15, 0.2, 0.1, -0.1, -0.15, 0.05, 0.1, 0.15, 0.3],
        description="List of 12 values representing the seasonal variation for each month",
    )
    growth_rate: float = Field(default=0.05, description="Annual growth rate")
    initial_investment: float = Field(default=100000, description="Initial investment")


class SimulationResult(BaseModel):
    month: int
    adjusted_sales: float
    royalties: float
    national_marketing: float
    fixed_costs: float
    variable_costs: float
    delivery_costs: float
    taxes: float
    local_marketing: float
    net_profit: float


class FinancialAnalysis(BaseModel):
    break_even_point: float
    roi: float = Field(default=0.0, description="Return on Investment (%)")
    contribution_margin: float
    contribution_margin_ratio: float

    @field_validator("roi")
    def round_roi(cls, v):
        return round(v, 2)
