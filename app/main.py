from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import logging
import time
import random
import os

# OpenTelemetry imports



app = FastAPI(title="Observability Demo", version="1.0.0")

# Set up Prometheus metrics
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Routes
import asyncio
@app.get("/")
async def read_root():
    await asyncio.sleep(random.uniform(0.2, 2.0))
    return {"Hello": "World"}

@app.get("/slow")
async def slow():
    delay = random.uniform(0.5, 3.0)
    await asyncio.sleep(delay)
    return {"message": f"Slow response after {delay:.2f} seconds"}

@app.get("/error")
async def error():
    await asyncio.sleep(random.uniform(0.2, 2.0))
    raise HTTPException(status_code=500, detail="Simulated error")

@app.get("/health")
async def health():
    await asyncio.sleep(random.uniform(0.2, 1.0))
    return {"status": "ok"}
