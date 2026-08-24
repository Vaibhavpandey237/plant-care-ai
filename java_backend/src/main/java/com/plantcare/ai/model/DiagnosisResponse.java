package com.plantcare.ai.model;

import java.util.List;
import java.util.Map;

public class DiagnosisResponse {
    private Long diagnosisId;
    private String imageName;
    private String topPrediction;
    private Double confidencePct;
    private Integer healthScore;
    private String severity;
    private boolean uncertain;
    private List<PredictionItem> predictions;
    private Map<String, Object> recommendations;
    private Map<String, Object> imageAnalysisMetrics;

    public DiagnosisResponse() {}

    public static class PredictionItem {
        private String label;
        private Double confidence;

        public PredictionItem() {}
        public PredictionItem(String label, Double confidence) {
            this.label = label;
            this.confidence = confidence;
        }

        public String getLabel() { return label; }
        public void setLabel(String label) { this.label = label; }
        public Double getConfidence() { return confidence; }
        public void setConfidence(Double confidence) { this.confidence = confidence; }
    }

    // Getters and Setters
    public Long getDiagnosisId() { return diagnosisId; }
    public void setDiagnosisId(Long diagnosisId) { this.diagnosisId = diagnosisId; }

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

    public boolean isUncertain() { return uncertain; }
    public void setUncertain(boolean uncertain) { this.uncertain = uncertain; }

    public List<PredictionItem> getPredictions() { return predictions; }
    public void setPredictions(List<PredictionItem> predictions) { this.predictions = predictions; }

    public Map<String, Object> getRecommendations() { return recommendations; }
    public void setRecommendations(Map<String, Object> recommendations) { this.recommendations = recommendations; }

    public Map<String, Object> getImageAnalysisMetrics() { return imageAnalysisMetrics; }
    public void setImageAnalysisMetrics(Map<String, Object> imageAnalysisMetrics) { this.imageAnalysisMetrics = imageAnalysisMetrics; }
}
