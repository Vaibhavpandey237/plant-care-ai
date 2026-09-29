# Contributing to PlantCare AI 🌿

Thank you for your interest in contributing to **PlantCare AI**! We welcome contributions from developers, designers, data scientists, and plant enthusiasts.

---

## 📌 Code of Conduct

Please be respectful, constructive, and inclusive in all discussions and pull requests.

---

## 🛠️ Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/Vaibhavpandey237/plant-care-ai.git
   cd plant-care-ai
   ```
3. **Create a branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/my-new-feature
   ```

---

## 🏗️ Project Structure

- **`src/`** — React 18 + Vite Frontend application.
- **`public/`** — Static assets and plant media.
- **`java_backend/`** — Spring Boot 3 + Deep Java Library (DJL) service.
- **`plant_care_ai/`** — Python + Flask + TensorFlow AI detection engine and CLI tools.

---

## 💻 Development Workflow

### Frontend (React + Vite)
```bash
npm install
npm run dev
```

### Python AI Engine
```bash
cd plant_care_ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Java Backend (Spring Boot)
```bash
cd java_backend
mvn clean install
mvn spring-boot:run
```

---

## 🧪 Running Tests

- **Python Tests**:
  ```bash
  cd plant_care_ai
  pytest tests/
  ```
- **Java Tests**:
  ```bash
  cd java_backend
  mvn test
  ```

---

## 🚀 Submitting a Pull Request

1. Commit your changes with clear, descriptive commit messages.
2. Ensure no cache, build, or temporary files are included (`git status`).
3. Push to your fork:
   ```bash
   git push origin feature/my-new-feature
   ```
4. Open a Pull Request on the main repository describing your changes in detail.

---

## 📄 License

By contributing to PlantCare AI, you agree that your contributions will be licensed under the [MIT License](LICENSE).
