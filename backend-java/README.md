# ☕ PlantCare AI — Enterprise Java Backend (Spring Boot 3 + DJL)

High-performance, enterprise-grade REST service for plant disease diagnosis, image processing, and history persistence built with Java 17, Spring Boot 3, and Deep Java Library (DJL).

---

## 🚀 Key Technologies

- **Java**: 17+ (LTS)
- **Framework**: [Spring Boot 3.2.3](https://spring.io/projects/spring-boot)
  - `spring-boot-starter-web`
  - `spring-boot-starter-data-jpa`
- **Deep Learning Engine**: [Deep Java Library (DJL) 0.26.0](https://djl.ai/)
  - `ai.djl.pytorch:pytorch-engine`
  - `ai.djl.pytorch:pytorch-model-zoo`
- **Database**: MySQL Connector / H2 In-Memory fallback
- **Build Tool**: Apache Maven

---

## 📂 Architecture & Package Layout

```
backend-java/
├── pom.xml                               # Maven project configuration & dependencies
└── src/
    └── main/
        ├── java/com/plantcare/ai/
        │   ├── PlantCareAiApplication.java # Spring Boot application entry point
        │   ├── Server.java               # Lightweight HTTP / fallback server
        │   ├── controller/
        │   │   └── DiagnosisController.java # REST Endpoints (/api/v1/diagnose, /api/v1/history)
        │   ├── model/
        │   │   ├── DiagnosisRecord.java   # JPA Entity for scan persistence
        │   │   └── DiagnosisResponse.java # DTO for diagnosis response & scores
        │   ├── repository/
        │   │   └── DiagnosisRepository.java # Spring Data JPA repository
        │   └── service/
        │       ├── DjlInferenceService.java    # Deep Java Library tensor classification
        │       └── ImageProcessingService.java # BufferedImage pre-processing & resizing
        └── resources/
            └── application.properties    # DataSource, JPA, and server port settings
```

---

## 🛠️ Quick Start

```bash
# 1. Build and install dependencies
mvn clean install

# 2. Run the Spring Boot server (port 8080)
mvn spring-boot:run

# 3. Run test cases
mvn test
```
