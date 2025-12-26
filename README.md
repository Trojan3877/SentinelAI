# 🛡️ Sentinel AI — L7 Production AI Inference Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![CUDA](https://img.shields.io/badge/NVIDIA-CUDA-success)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-red)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🔥 Overview

**Sentinel AI** is a **production-grade AI inference and observability platform** designed for **GPU-accelerated Large Language Model (LLM) workloads**.

Built using **FastAPI, NVIDIA CUDA, Llama 3, MLflow, Prometheus, Docker, Render, and n8n**, Sentinel AI demonstrates **L7-level system design** aligned with Big Tech and Big AI engineering standards.

This project emphasizes:
- Reliability
- Monitoring-first architecture
- Secure, scalable inference
- Cloud + GPU deployment readiness

---

## 🧠 System Architecture

![Sentinel AI Architecture](assets/sentinel_ai_system_architecture.png)

---

## ⚙️ Tech Stack

### Backend & AI
- **FastAPI** – High-performance API layer
- **Python 3.11**
- **Meta Llama 3 (8B)** – GPU-accelerated inference
- **PyTorch + Transformers**

### Infrastructure
- **Docker (CUDA-enabled)**
- **Render GPU deployment**
- **NVIDIA CUDA Runtime**

### Observability & Ops
- **MLflow** – Experiment & inference tracking
- **Prometheus** – Metrics & monitoring
- **n8n** – AI workflow automation

### Security
- OAuth2 + JWT authentication
- Rate limiting (SlowAPI)

---

## 🚀 Quick Start

```bash
git clone https://github.com/Trojan3877/Sentinel-AI
cd Sentinel-AI

docker build -t sentinel-ai .
docker run --gpus all -p 8000:8000 sentinel-ai
http://localhost:8000


📈 Production Features

✅ GPU-backed LLM inference

✅ FastAPI + async architecture

✅ Auth & rate limiting

✅ MLflow experiment tracking

✅ Prometheus metrics

✅ CI/CD ready

✅ Cloud & GPU deployable

🧩 Project Status

Engineering Level: L7 (Senior / Staff-level system design)

Readiness: Internship, New Grad, Research, MLOps, AI Engineer

Target Roles:

AI Engineer

ML Engineer

MLOps Engineer

Software Engineer (Backend / Platform)
👤 Author

Corey Leath
Senior Undergraduate — Software Development (Web & Mobile)
Aspiring AI Engineer | Production ML Systems
https://github.com/Trojan3877
