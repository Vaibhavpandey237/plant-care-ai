# 🐍 PlantCare AI — Python AI Engine & Flask Service

Deep learning model training, image processing, disease diagnosis, and treatment recommendation engine powered by TensorFlow, OpenCV, and Flask.

---

## 🚀 Key Technologies

- **Python**: 3.10+
- **Deep Learning**: TensorFlow / Keras, Scikit-learn
- **Image Processing**: Pillow, OpenCV / NumPy
- **Web API**: Flask 2.3+, Werkzeug
- **Database ORM**: SQLAlchemy / SQLite
- **Testing**: Pytest, Pytest-Flask

---

## 📂 Architecture & Directory Layout

```
backend-python/
├── .env.example              # Environment configuration template
├── requirements.txt          # Python dependencies
├── setup.py                  # Package installer
├── main.py                   # Flask Application entry point
├── config.py                 # Configuration loader
├── run_server.py             # Standalone development server runner
├── app/
│   ├── api.py                # REST API routes
│   ├── routes/               # Modular Flask Blueprints (auth, diagnose, history, pages)
│   ├── static/               # CSS & JavaScript for server-rendered views
│   └── templates/            # Jinja2 HTML templates
├── core/
│   ├── care_recommender.py   # Disease remedy & fertilizer expert system
│   ├── classifier.py         # CNN leaf classifier
│   ├── health.py             # Plant health score calculator
│   ├── model.py              # Neural network architecture definitions
│   ├── preprocess.py         # Image resizing, normalization, and tensor conversion
│   ├── species.py            # Plant species catalog & taxonomies
│   └── trainer.py            # Model training & validation pipelines
├── database/
│   ├── db.py                 # SQLite engine & database connection
│   └── repository.py         # CRUD repository for users & scan history
├── scripts/
│   ├── build_demo_model.py   # Quick demo model generator
│   ├── create_demo_leaves.py # Synthetic demo leaves generator
│   ├── download_dataset.py   # Dataset fetcher
│   ├── export_report.py      # Diagnostic report exporter
│   └── train_model.py        # Model training script
├── demo/                     # Demo leaf images for test scans
├── tests/                    # Comprehensive unit tests
└── data/
    ├── models/               # Model weights (.h5) & labels.json
    └── uploads/              # Temporary upload storage (.gitkeep)
```

---

## 🛠️ Quick Start

```bash
# 1. Create and activate a virtual environment
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
# source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the Flask server (port 5000)
python main.py

# 4. Run tests
pytest tests/
```
