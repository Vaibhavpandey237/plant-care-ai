# 🌿 Plant Care AI Detection System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.13-orange.svg)](https://tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end, production-ready **Plant Care AI Detection System** built in Python. The system detects plant diseases from leaf images using MobileNetV2 transfer learning, scores overall plant health (0–100), classifies severity levels, and generates detailed, multi-category care recommendations (chemical, organic, cultural treatment, watering, sunlight, fertilizer, and prevention).

Includes a modern **Web Dashboard**, a complete **REST API**, a comprehensive **CLI Tool**, and persistent **SQLite storage**.

---

## 📐 Architecture Overview

```
                          ┌────────────────────────────────┐
                          │    User Interface / Clients    │
                          ├──────────────┬─────────────────┤
                          │  Web Browser │   CLI Tool      │
                          │ (HTML5/CSS3) │   (main.py)     │
                          └──────┬───────┴────────┬────────┘
                                 │ HTTP           │ Python API
                                 ▼                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                        Plant Care AI Application                          │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│   ┌─────────────────────┐    ┌─────────────────┐    ┌─────────────────┐   │
│   │ Flask Web Server    │    │ REST API        │    │ SQLite Database │   │
│   │ (app/routes)        │    │ (/api/*)        │    │ (plant_care.db) │   │
│   └──────────┬──────────┘    └────────┬────────┘    └────────▲────────┘   │
│              │                        │                      │            │
│              └───────────┬────────────┘                      │ CRUD       │
│                          ▼                                   │            │
│   ┌──────────────────────────────────────────────────────────┴────────┐   │
│   │                 Core Pipeline (core/classifier.py)                 │   │
│   ├───────────────────┬───────────────────┬───────────────────────────┤   │
│   │ Image Preprocessor│ Inference Model   │ Health Scoring & Severity │   │
│   │ (core/preprocess) │ (MobileNetV2 .h5) │ (core/health.py)          │   │
│   └───────────────────┴─────────┬─────────┴───────────────────────────┘   │
│                                 │                                         │
│                                 ▼                                         │
│   ┌───────────────────────────────────────────────────────────────────┐   │
│   │           Care Recommendation Engine (core/care_recommender.py)   │   │
│   └───────────────────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

- **Deep Learning Classification:** Transfer learning with MobileNetV2 fine-tuned on 38+ PlantVillage leaf disease classes.
- **Health Assessment (0–100 Score):** Dynamic scoring derived from classification confidence and condition status.
- **Severity Levels:** Auto-categorizes diagnosis as `LOW`, `MEDIUM`, or `HIGH` severity.
- **Actionable Care Plans:** Detailed recommendations covering chemical treatment, organic remedies, cultural practices, watering, sunlight, and fertilizer advice.
- **Full REST API:** 7 JSON endpoints with strict request validation, error envelopes, and HTTP status codes.
- **Web Dashboard:** Interactive drag-and-drop file upload, real-time image preview, health score gauge, and diagnosis history table.
- **CLI Interface:** Complete command-line management for diagnosis, training, server launch, history inspection, and CSV export.
- **Offline & Local First:** Zero runtime external API dependencies. All models and assets run locally.

---

## 🛠️ Project Structure

```
plant_care_ai/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── setup.py                  # Package installation file
├── .env.example              # Environment variables template
├── config.py                 # Centralized configuration
├── main.py                   # CLI entry point
├── run_server.py             # Web server entry point
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── api.py                # REST API endpoints
│   ├── routes/               # Web dashboard routes
│   │   ├── __init__.py
│   │   ├── diagnose.py
│   │   ├── plants.py
│   │   └── history.py
│   ├── templates/            # Jinja2 HTML templates
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   ├── result.html
│   │   └── plants.html
│   └── static/               # Static web assets
│       ├── css/style.css
│       └── js/script.js
├── core/                     # Machine learning pipeline
│   ├── __init__.py
│   ├── preprocess.py         # Image preprocessing & normalization
│   ├── model.py              # Model loading & inference singleton
│   ├── classifier.py         # High-level diagnose() API
│   ├── health.py             # Health score & severity logic
│   ├── care_recommender.py   # Care knowledge base & engine
│   ├── species.py            # Botanical knowledge base
│   └── trainer.py            # MobileNetV2 transfer learning trainer
├── data/
│   ├── raw/                  # Downloaded dataset directory
│   ├── processed/            # Processed artifacts
│   └── models/               # Saved plant_model.h5 & labels.json
├── database/                 # Persistence layer
│   ├── __init__.py
│   ├── db.py                 # SQLite connection & schema init
│   └── repository.py         # CRUD repository
├── demo/                     # Demo leaf images for quick offline testing
│   ├── leaf1.png             # Synthetic healthy leaf
│   ├── leaf2.png             # Synthetic diseased leaf (scab)
│   └── leaf3.png             # Synthetic diseased leaf (rot)
├── utils/                    # Shared utilities
│   ├── __init__.py
│   ├── logger.py             # Centralized logging with file rotation
│   └── validators.py         # Upload and parameter validators
├── scripts/                  # Executable helper scripts
│   ├── download_dataset.py   # Dataset downloader helper
│   ├── train_model.py        # Model training script
│   └── export_report.py      # CSV export script
└── tests/                    # Unit and integration test suite
    ├── __init__.py
    ├── test_preprocess.py
    ├── test_health.py
    ├── test_recommender.py
    └── test_api.py
```

---

## 🚀 Quick Start Guide

### 1. Environment Setup

```bash
# Clone or navigate to the project directory
cd plant_care_ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Initialize Database & Generate Demo Images

```bash
# Initialize SQLite database with seed data
python main.py init-db

# Generate synthetic demo leaf images in demo/
python scripts/create_demo_leaves.py
```

---

## 📦 Dataset Download & Model Training

### Downloading PlantVillage Dataset

The system uses the free **PlantVillage Dataset** from Kaggle (~54,000 leaf images across 38 classes).

**Option A: Automatic Download via Kaggle CLI**
```bash
python main.py download-data --auto-download
```

**Option B: Manual Download (Recommended)**
1. Visit [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset).
2. Download `plantvillage-dataset.zip`.
3. Extract the class subdirectories into `data/raw/` (e.g., `data/raw/Apple___Apple_scab`, `data/raw/Tomato___healthy`, etc.).

### Training the Model

Train the MobileNetV2 transfer learning model:

```bash
# Full training on complete dataset (takes ~30-60 mins on CPU / 5 mins on GPU)
python main.py train --epochs 5 --batch-size 32

# Fast Demo Mode (trained on 20% subset in ~2 minutes for quick testing)
python main.py train --subset 0.2 --epochs 2
```

Training saves the following artifacts:
- `data/models/plant_model.h5` — Saved Keras model checkpoint
- `data/models/labels.json` — Class label index mapping
- `data/models/training_curves.png` — Accuracy & Loss curves
- `data/models/confusion_matrix.png` — Normalized evaluation matrix

---

## 🌐 Running the Web Server & Dashboard

Start the web server on `http://127.0.0.1:5000`:

```bash
python run_server.py
```
*Or via CLI:*
```bash
python main.py serve --port 5000
```

Open `http://127.0.0.1:5000` in your browser to access:
- **Homepage (`/`):** Upload leaf images via drag-and-drop or file picker.
- **Dashboard (`/dashboard`):** View diagnosis history, health statistics, and top diseases.
- **Species Guide (`/plants`):** Explore botanical care guides.

---

## 💻 CLI Usage Examples

```bash
# 1. Diagnose a demo leaf image
python main.py diagnose --image demo/leaf1.png --top 5

# 2. View recent diagnosis history
python main.py history --limit 10

# 3. Export diagnosis records to CSV
python main.py export-csv --out diagnoses_report.csv
```

---

## 📡 REST API Reference

All API responses follow a unified JSON envelope:
```json
{
  "success": true,
  "data": { ... },
  "error": null
}
```

### Endpoints Table

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Service health & model status |
| `POST` | `/api/diagnose` | Upload leaf image for diagnosis |
| `GET` | `/api/history` | Paginated diagnosis history |
| `GET` | `/api/history/<id>` | Detail of single diagnosis record |
| `DELETE` | `/api/history/<id>` | Delete a diagnosis record |
| `GET` | `/api/classes` | List supported classes & metadata |
| `GET` | `/api/recommendations/<class_name>` | Get care plan for a class |

### `curl` Usage Examples

#### 1. Diagnose an Image (`POST /api/diagnose`)
```bash
curl -X POST -F "image=@demo/leaf1.png" http://127.0.0.1:5000/api/diagnose
```

#### 2. Service Health (`GET /api/health`)
```bash
curl http://127.0.0.1:5000/api/health
```

#### 3. View History (`GET /api/history`)
```bash
curl "http://127.0.0.1:5000/api/history?page=1&per_page=5"
```

#### 4. Get Care Info (`GET /api/recommendations/Tomato___Late_blight`)
```bash
curl http://127.0.0.1:5000/api/recommendations/Tomato___Late_blight
```

---

## 🧪 Testing

Run unit and integration tests using `pytest`:

```bash
# Run all tests quietly
pytest -q

# Run with verbose output
pytest -v
```

All 6+ tests run offline and pass cleanly without requiring a pre-trained model file.

---

## ❓ Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| `Model not found. Run: python main.py train` | Model `.h5` file has not been created | Run `python main.py train --subset 0.2 --epochs 2` |
| `File too large (X MB). Maximum is 10 MB` | Uploaded image exceeds size limit | Resize image or raise `MAX_UPLOAD_MB` in `.env` |
| `Unsupported file type .xyz` | Non-image extension | Convert image to `.jpg` or `.png` |
| `Dataset not found at data/raw` | Dataset folder is empty | Download PlantVillage dataset and place folders into `data/raw/` |

---

## 🗺️ Project Roadmap

- [ ] Mobile app integration (React Native / Flutter API integration).
- [ ] Multi-leaf batch upload support.
- [ ] Weather API integration for local fungal outbreak alerts.
- [ ] Model quantization to ONNX/TFLite for edge devices (Raspberry Pi / Jetson).

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
