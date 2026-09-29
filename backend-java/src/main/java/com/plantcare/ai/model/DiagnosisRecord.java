package com.plantcare.ai.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "diagnoses")
public class DiagnosisRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "image_name", nullable = false)
    private String imageName;

    @Column(name = "top_prediction", nullable = false)
    private String topPrediction;

    @Column(name = "confidence_pct", nullable = false)
    private Double confidencePct;

    @Column(name = "health_score", nullable = false)
    private Integer healthScore;

    @Column(name = "severity", nullable = false)
    private String severity;

    @Column(name = "recommendations_json", columnDefinition = "TEXT")
    private String recommendationsJson;

    @Column(name = "created_at", nullable = false)
    private LocalDateTime createdAt;

    public DiagnosisRecord() {
        this.createdAt = LocalDateTime.now();
    }

    public DiagnosisRecord(String imageName, String topPrediction, Double confidencePct, Integer healthScore, String severity, String recommendationsJson) {
        this.imageName = imageName;
        this.topPrediction = topPrediction;
        this.confidencePct = confidencePct;
        this.healthScore = healthScore;
        this.severity = severity;
        this.recommendationsJson = recommendationsJson;
        this.createdAt = LocalDateTime.now();
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getImageName() { return imageName; }
    public void setImageName(String imageName) { this.imageName = imageName; }

    public String getTopPrediction() { return topPrediction; }
    public void setTopPrediction(String topPrediction) { this.topPrediction = topPrediction; }

    public Double getConfidencePct() { return confidencePct; }
    public void setConfidencePct(Double confidencePct) { this.confidencePct = confidencePct; }

    public Integer getHealthScore() { return healthScore; }
    public void setHealthScore(Integer healthScore) { this.healthScore = healthScore; }

    public String getSeverity() { return severity; }
    public void setSeverity(String severity) { this.severity = severity; }

    public String getRecommendationsJson() { return recommendationsJson; }
    public void setRecommendationsJson(String recommendationsJson) { this.recommendationsJson = recommendationsJson; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
