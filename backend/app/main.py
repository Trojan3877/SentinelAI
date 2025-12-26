# backend/app/main.py
from fastapi import FastAPI
import torch

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "cuda": torch.cuda.is_available()}

@app.post("/predict")
def predict(data: list[float]):
    tensor = torch.tensor(data).cuda()
    result = tensor.mean().item()
    return {"prediction": result}

import mlflow
import mlflow.pytorch

mlflow.set_tracking_uri("http://mlflow:5000")

with mlflow.start_run():
    mlflow.log_param("model", "cuda-inference")
    mlflow.log_metric("latency_ms", 12.4)

from prometheus_client import Counter, generate_latest
from fastapi import Response

REQUESTS = Counter("requests_total", "Total requests")

@app.middleware("http")
async def metrics_middleware(request, call_next):
    REQUESTS.inc()
    return await call_next(request)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
