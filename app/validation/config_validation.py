from typing import Any, Dict


def validate_config(config: Dict[str, Any]) -> None:
    """Validates the configuration values."""
    required_keys = [
        "BASE_MONTHLY_SALES",
        "SUPPLY_COST",
        "PACKAGING_COST",
        "DELIVERY_FEES",
        "ROYALTY_PERCENTAGE",
        "NATIONAL_MARKETING_PERCENTAGE",
        "TAX_PERCENTAGE",
        "FIXED_COSTS",
        "LOCAL_MARKETING_COST",
    ]

    for key in required_keys:
        if key not in config:
            raise KeyError(f"Key missing in the configuration: {key}")
        if not isinstance(config[key], (int, float)):
            raise TypeError(f"{key} must be a number. Received: {type(config[key])}.")
