from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routers import api

app = FastAPI(
    title="Financial Simulation API",
    version="0.0.1",
    description="A Financial Simulation API é uma aplicação desenvolvida com FastAPI que permite"
    " simular resultados financeiros com base em vendas mensais, sazonalidade, "
    "taxa de crescimento e outros parâmetros financeiros. A API fornece endpoints"
    " para simular vendas, analisar resultados financeiros e gerar gráficos"
    " baseados nas simulações.",
)
app.include_router(api.router, prefix="/api/v1")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "details": str(exc)},
    )


@app.get("/")
async def root():
    return {"message": "Welcome to the Financial Simulation API"}
