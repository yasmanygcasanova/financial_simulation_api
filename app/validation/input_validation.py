from typing import List

from .exceptions import InvalidInputError


def validate_seasonality(seasonality: List[float]) -> None:
    """Validates that the seasonality list contains exactly 12 values and that all are between -1 and 1."""
    if len(seasonality) != 12:
        raise InvalidInputError("Seasonality must contain exactly 12 values.")

    for value in seasonality:
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Invalid value in seasonality: {value}. It must be a number."
            )
        if value < -1 or value > 1:
            raise InvalidInputError("Seasonality values must be between -1 and 1.")


def validate_growth_rate(growth_rate: float) -> None:
    """Validates that the growth rate is between 0 (0%) and 1 (100%)."""
    if not isinstance(growth_rate, (int, float)):
        raise TypeError("Growth rate must be a number.")
    if growth_rate < 0 or growth_rate > 1:
        raise InvalidInputError("Growth rate must be between 0 (0%) and 1 (100%).")


def validate_initial_investment(initial_investment: float) -> None:
    """Validates that the initial investment is a non-negative number."""
    if not isinstance(initial_investment, (int, float)):
        raise TypeError("Initial investment must be a number.")
    if initial_investment < 0:
        raise InvalidInputError("Initial investment cannot be negative.")
