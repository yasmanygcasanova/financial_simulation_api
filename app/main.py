from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .analysis import calculate_monthly_growth_rate, perform_financial_analysis
from .config import load_config
from .models import FinancialAnalysis, SimulationInput, SimulationResult
from .plotting import plot_results
from .simulation import (
    calculate_growth_adjusted_sales,
    calculate_monthly_results,
    get_seasonality,
)
from .validation.config_validation import validate_config
from .validation.exceptions import ConfigurationError, InvalidInputError
from .validation.input_validation import (
    validate_growth_rate,
    validate_initial_investment,
    validate_seasonality,
)

app = FastAPI(
    title="Financial Simulation API",
    version="0.0.1",
    description="A Financial Simulation API é uma aplicação desenvolvida com FastAPI que permite"
    " simular resultados financeiros com base em vendas mensais, sazonalidade, "
    "taxa de crescimento e outros parâmetros financeiros. A API fornece endpoints"
    " para simular vendas, analisar resultados financeiros e gerar gráficos"
    " baseados nas simulações.",
)


# Load and validate the configuration at the start
try:
    config = load_config()
    validate_config(config)
except ConfigurationError as e:
    print(f"Error loading configuration: {str(e)}")
    exit(1)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "details": str(exc)},
    )


@app.post("/simulate", response_model=List[SimulationResult])
async def simulate(input_data: SimulationInput):
    try:
        # Validate user inputs
        validate_seasonality(input_data.seasonality)
        validate_growth_rate(input_data.growth_rate)
        validate_initial_investment(input_data.initial_investment)

        seasonality = get_seasonality(",".join(map(str, input_data.seasonality)))
        results = []
        for month in range(1, 13):
            growth_adjusted_sales = calculate_growth_adjusted_sales(
                config["BASE_MONTHLY_SALES"], input_data.growth_rate, month
            )
            result = calculate_monthly_results(
                month, growth_adjusted_sales, seasonality, config
            )
            results.append(SimulationResult(**result))
        return results

    except (InvalidInputError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/analyze", response_model=FinancialAnalysis)
async def analyze(input_data: SimulationInput):
    try:
        # Validate user inputs
        validate_seasonality(input_data.seasonality)
        validate_growth_rate(input_data.growth_rate)

        simulation_results = await simulate(input_data)
        analysis = perform_financial_analysis(
            [dict(r) for r in simulation_results], input_data.initial_investment
        )
        return FinancialAnalysis(**analysis)

    except (InvalidInputError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/growth-rate")
async def growth_rate(input_data: SimulationInput):
    try:
        # Validate user inputs
        validate_seasonality(input_data.seasonality)
        validate_growth_rate(input_data.growth_rate)

        simulation_results = await simulate(input_data)
        monthly_growth = calculate_monthly_growth_rate(
            [dict(r) for r in simulation_results]
        )
        formatted_growth = round(monthly_growth, 2)
        return {"monthly_growth_rate": formatted_growth}

    except (InvalidInputError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/plot")
async def plot(input_data: SimulationInput):
    try:
        # Validate user inputs
        validate_seasonality(input_data.seasonality)
        validate_growth_rate(input_data.growth_rate)

        simulation_results = await simulate(input_data)
        plot_image = plot_results([dict(r) for r in simulation_results])
        return JSONResponse(content={"image": plot_image})

    except (InvalidInputError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the Financial Simulation API"}
