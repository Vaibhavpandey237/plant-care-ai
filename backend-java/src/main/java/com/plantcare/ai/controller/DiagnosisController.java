package com.plantcare.ai.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.plantcare.ai.model.DiagnosisRecord;
import com.plantcare.ai.model.DiagnosisResponse;
import com.plantcare.ai.repository.DiagnosisRepository;
import com.plantcare.ai.service.DjlInferenceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping
@CrossOrigin(origins = "*")
public class DiagnosisController {

    @Autowired
    private DjlInferenceService djlInferenceService;

    @Autowired
    private DiagnosisRepository diagnosisRepository;

    private final ObjectMapper objectMapper = new ObjectMapper();

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> checkHealth() {
        Map<String, Object> status = new HashMap<>();
        status.put("status", "UP");
        status.put("system", "Plant Care AI Java Backend");
        status.put("aiEngine", "Deep Java Library (DJL)");
        status.put("framework", "Spring Boot 3.2.3");
        return ResponseEntity.ok(status);
    }

    @PostMapping(value = "/diagnose", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<DiagnosisResponse> diagnosePlant(@RequestParam("image") MultipartFile file) {
        if (file.isEmpty()) {
            return ResponseEntity.badRequest().build();
        }

        try {
            byte[] bytes = file.getBytes();
            DiagnosisResponse response = djlInferenceService.diagnoseImage(bytes, file.getOriginalFilename());

            // Save record in MySQL DB
            try {
                String recsJson = objectMapper.writeValueAsString(response.getRecommendations());
                DiagnosisRecord record = new DiagnosisRecord(
                    response.getImageName(),
                    response.getTopPrediction(),
                    response.getConfidencePct(),
                    response.getHealthScore(),
                    response.getSeverity(),
                    recsJson
                );
                DiagnosisRecord saved = diagnosisRepository.save(record);
                response.setDiagnosisId(saved.getId());
            } catch (Exception dbEx) {
                System.err.println("⚠️ MySQL Database notice: " + dbEx.getMessage());
            }

            return ResponseEntity.ok(response);

        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    @GetMapping("/history")
    public ResponseEntity<List<DiagnosisRecord>> getHistory() {
        try {
            List<DiagnosisRecord> records = diagnosisRepository.findTop10ByOrderByCreatedAtDesc();
            return ResponseEntity.ok(records);
        } catch (Exception e) {
            return ResponseEntity.ok(List.of());
        }
    }
}
