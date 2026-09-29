# 🏛️ PlantCare AI — Monorepo Architecture Specification

## 🌐 Overview

PlantCare AI is organized as a modular, three-tier monorepo consisting of:
1. **Frontend**: React 18 + Vite SPA client with component modularity.
2. **Backend (Java)**: Spring Boot 3 + Deep Java Library (DJL) enterprise REST microservice.
3. **Backend (Python)**: Flask + TensorFlow / Keras deep learning training and inference engine.

---

## 🏗️ 3-Tier Architecture Diagram

```
                        ┌──────────────────────────────────────────────┐
                        │              Frontend Client                 │
                        │           (React 18 + Vite SPA)              │
                        │                                              │
                        │  • Modular UI Views (Dashboard, Diagnosis)   │
                        │  • Mandi & Government MSP Price Tracker      │
                        │  • Verified Remedy & Fertilizer Catalog      │
                        │  • AI Botanist Chatbot & Garden Reminders    │
                        └──────────────────────┬───────────────────────┘
                                               │
                                       HTTP / JSON REST
                                               │
               ┌───────────────────────────────┴──────────────────────────────┐
               │                                                              │
               ▼                                                              ▼
┌──────────────────────────────────────────────┐     ┌──────────────────────────────────────────────┐
│           Java Spring Boot Backend           │     │            Python AI / ML Engine             │
│              (Port 8080)                     │     │                 (Port 5000)                  │
│                                              │     │                                              │
│  • Spring Boot 3 & Spring Data JPA           │     │  • Flask REST API & Blueprint Routing        │
│  • Deep Java Library (DJL) PyTorch Runtime   │     │  • TensorFlow / Keras CNN Model Inference    │
│  • BufferedImage Image Processing Service    │     │  • Fertilizer & Remedy Expert System         │
│  • MySQL / H2 Persistence                    │     │  • Automated Dataset & Training Pipelines    │
└──────────────────────────────────────────────┘     └──────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
plant-care-ai/
├── .github/
│   ├── workflows/             # Automated CI for Frontend, Python, and Java
│   │   ├── frontend-ci.yml
│   │   ├── python-ci.yml
│   │   └── java-ci.yml
│   └── pull_request_template.md
├── frontend/                  # React 18 + Vite Frontend Application
│   ├── public/                # Static assets & favicon
│   ├── src/                   # Modular React source code
│   │   ├── components/        # View & feature components
│   │   ├── data/              # Datasets & initial states
│   │   ├── services/          # REST API integration
│   │   ├── App.jsx            # Main app container
│   │   ├── index.css          # Design system & styles
│   │   └── main.jsx           # App entry point
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── backend-java/              # Spring Boot 3 + DJL AI Inference Service
│   ├── pom.xml
│   ├── README.md
│   └── src/
├── backend-python/            # Python Flask + TensorFlow Deep Learning Engine
│   ├── .env.example
│   ├── requirements.txt
│   ├── setup.py
│   ├── README.md
│   ├── main.py
│   ├── app/
│   ├── core/
│   ├── database/
│   ├── scripts/
│   ├── tests/
│   └── data/
├── docs/                      # Technical Documentation
│   └── architecture.md
├── .env.example               # Root environment configuration
├── .gitignore                 # Universal root gitignore
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Guidelines for open-source contributors
├── README.md                  # Master Monorepo Documentation
└── vercel.json                # Deployment configuration
```
