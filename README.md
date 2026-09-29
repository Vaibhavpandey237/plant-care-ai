# 🌱 PlantCare AI — Intelligent Plant Disease Detection & Smart Plant Care Assistant

<p align="center">
  <a href="https://plant-care-ai-phi.vercel.app" target="_blank">
    <img src="https://img.shields.io/badge/🌱%20Live%20Demo-Vercel-success?style=for-the-badge" alt="Live Demo" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-React%2018%20%2B%20Vite-61DAFB?style=for-the-badge&logo=react" alt="React" />
  <img src="https://img.shields.io/badge/Backend%20(Java)-Spring%20Boot%203%20%2B%20DJL-F89820?style=for-the-badge&logo=openjdk" alt="Java Spring Boot" />
  <img src="https://img.shields.io/badge/Backend%20(Python)-TensorFlow%20%2B%20Flask-3776AB?style=for-the-badge&logo=python" alt="Python Flask" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  <b>🌿 A production-ready, 3-tier monorepo architecture for plant disease detection, agricultural price tracking, and intelligent plant care.</b>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Monorepo Architecture](#-monorepo-architecture)
- [Project Directory Structure](#-project-directory-structure)
- [Quick Start Guide](#-quick-start-guide)
  - [1. Frontend (`frontend/`)](#1-frontend-frontend)
  - [2. Java Enterprise Backend (`backend-java/`)](#2-java-enterprise-backend-backend-java)
  - [3. Python AI & ML Engine (`backend-python/`)](#3-python-ai--ml-engine-backend-python)
- [Deployment](#-deployment)
- [CI / CD Workflows](#-ci--cd-workflows)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**PlantCare AI** is an intelligent agricultural diagnosis and plant-care platform. By analyzing leaf photographs using deep learning computer vision models, it accurately identifies plant diseases, evaluates health severity, and provides immediate, actionable treatment recommendations, verified product remedies, and long-term care schedules.

---

## 🧠 Monorepo Architecture

```
               ┌──────────────────────────────────────────────────┐
               │              frontend/ (React 18 + Vite)         │
               │        Modular Single Page Application (SPA)     │
               └────────────────────────┬─────────────────────────┘
                                        │
                             REST API / HTTP Uploads
                                        │
         ┌──────────────────────────────┴──────────────────────────────┐
         │                                                             │
         ▼                                                             ▼
┌──────────────────────────────────────┐     ┌──────────────────────────────────────┐
│     backend-java/ (Spring Boot 3)    │     │       backend-python/ (Flask AI)     │
│   • Deep Java Library (DJL) PyTorch  │     │   • TensorFlow / Keras CNN Models    │
│   • BufferedImage Preprocessing      │     │   • Disease & Fertilizer Recommender │
│   • MySQL / H2 JPA Persistence       │     │   • Model Training & CLI Scripts     │
└──────────────────────────────────────┘     └──────────────────────────────────────┘
```

---

## 📁 Project Directory Structure

```
plant-care-ai/
├── .github/
│   ├── workflows/             # Automated CI for Frontend, Python, and Java
│   │   ├── frontend-ci.yml
│   │   ├── python-ci.yml
│   │   └── java-ci.yml
│   └── pull_request_template.md
├── frontend/                  # 🌿 React 18 + Vite Web Application
│   ├── public/                # Static assets, plant images & favicon
│   ├── src/
│   │   ├── components/        # Modular UI components (auth, diagnosis, garden, prices, etc.)
│   │   ├── data/              # Datasets (products, crop prices, plant profiles)
│   │   ├── services/          # Centralized API service
│   │   ├── App.jsx            # Orchestration container
│   │   ├── index.css          # Design system & dark/light theme tokens
│   │   └── main.jsx           # App entry point
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── backend-java/              # ☕ Spring Boot 3 + DJL Deep Learning Microservice
│   ├── pom.xml                # Maven configuration (Spring Boot, DJL PyTorch, MySQL/H2)
│   ├── README.md
│   └── src/main/
│       ├── java/com/plantcare/ai/ (controllers, services, entities, repositories)
│       └── resources/ (application.properties)
├── backend-python/            # 🐍 Python Flask + TensorFlow ML Engine
│   ├── .env.example
│   ├── requirements.txt
│   ├── setup.py
│   ├── README.md
│   ├── main.py                # Flask server entry point
│   ├── config.py
│   ├── app/                   # Blueprints, routes, templates, static
│   ├── core/                  # Classifier, recommender, health scoring, models
│   ├── database/              # SQLite / SQLAlchemy models
│   ├── scripts/               # Training, demo generation, dataset scripts
│   ├── demo/                  # Demo leaf images
│   ├── tests/                 # Pytest test suite
│   └── data/
│       ├── models/            # Model weights & labels.json
│       └── uploads/           # Upload directory (.gitkeep)
├── docs/                      # 📖 Documentation
│   └── architecture.md        # Technical architecture specification
├── .env.example               # Root configuration template
├── .gitignore                 # Universal Git ignore rules
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Contribution guidelines
├── README.md                  # Project README
└── vercel.json                # Vercel deployment configuration
```

---

## 🚀 Quick Start Guide

### 1. Frontend (`frontend/`)

```bash
cd frontend

# Install dependencies
npm install

# Start local dev server (http://localhost:5174)
npm run dev

# Build for production
npm run build
```

---

### 2. Java Enterprise Backend (`backend-java/`)

```bash
cd backend-java

# Clean build and run tests
mvn clean install

# Start the Spring Boot service (http://localhost:8080)
mvn spring-boot:run
```

---

### 3. Python AI & ML Engine (`backend-python/`)

```bash
cd backend-python

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask AI server (http://localhost:5000)
python main.py

# Run test cases
pytest tests/
```

---

## 🚢 Deployment

### Frontend (Vercel)
The repository includes a top-level `vercel.json` configured for monorepo deployments to **Vercel** with zero-config builds.

---

## 🤖 CI / CD Workflows

Automated GitHub Actions workflows are located in [`.github/workflows/`](.github/workflows/):
- **`frontend-ci.yml`**: Builds and validates the React application on push and pull requests.
- **`python-ci.yml`**: Sets up Python and executes the `pytest` suite.
- **`java-ci.yml`**: Compiles Java with Maven and runs Spring Boot unit tests.

---

## 🤝 Contributing

Contributions are welcome! Please check out [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the pull request process.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
