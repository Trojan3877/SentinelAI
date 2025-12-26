# SentinelAI 🚨  
### Production-Grade AI Inference & Monitoring Platform

![CI](https://github.com/Trojan3877/SentinelAI/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Kubernetes](https://img.shields.io/badge/kubernetes-orchestrated-blue)
![CUDA](https://img.shields.io/badge/NVIDIA-CUDA-green)
![LLM](https://img.shields.io/badge/LLM-Llama%203-orange)
![FastAPI](https://img.shields.io/badge/API-FastAPI-teal)
![TypeScript](https://img.shields.io/badge/frontend-TypeScript-blue)
![MLflow](https://img.shields.io/badge/MLflow-tracking-purple)
![Prometheus](https://img.shields.io/badge/metrics-Prometheus-red)
![Level](https://img.shields.io/badge/Portfolio-L7%20Production-success)

---

## 🚀 Overview
SentinelAI is a **full-stack, GPU-accelerated AI platform** designed for **secure inference, monitoring, and observability** using modern MLOps and platform engineering practices.

Built to **Big Tech production standards**, not coursework demos.

---

## 🧠 System Architecture


    U --> FE
    FE --> API
    API --> AUTH
    AUTH --> LLM
    LLM --> GPU
    GPU --> K8S
    API --> ML
    API --> MET
    CI --> RENDER
    RENDER --> K8S
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4cbc93b4-a7ba-4615-9ddb-82f06745151a" />


🧰 Tech Stack
Frontend

Next.js (TypeScript)

Tailwind CSS

Streamlit (Live Metrics Dashboard)

Backend

FastAPI

Llama 3 (CUDA)

Auth + Rate Limiting

MLflow Experiment Tracking

Infrastructure

Docker

Kubernetes (GPU scheduling)

Prometheus

Render Deployment

GitHub Actions CI/CD

⚡ Quick Start (Local)
docker compose up --build


API → http://localhost:8000

UI → http://localhost:3000

☸️ Kubernetes Deployment
kubectl apply -f k8s/


Supports NVIDIA GPU nodes, metrics scraping, and horizontal scaling.

🧪 Testing
pytest tests/


Includes:

Health checks

Auth validation

Rate limiting

LLM inference validation

📊 Observability

/metrics → Prometheus

MLflow UI → experiment tracking

Streamlit → live dashboard

🎯 Why SentinelAI

✔ Production-ready
✔ GPU-accelerated
✔ Full-stack TypeScript + Python
✔ MLOps + Platform Engineering
✔ Recruiter-credible system design

👤 Author

Corey Leath
Senior Software Engineering Student
AI / ML / Platform Engineering
https://github.com/Trojan3877
