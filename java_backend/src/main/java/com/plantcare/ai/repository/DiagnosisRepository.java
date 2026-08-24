package com.plantcare.ai.repository;

import com.plantcare.ai.model.DiagnosisRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DiagnosisRepository extends JpaRepository<DiagnosisRecord, Long> {
    List<DiagnosisRecord> findTop10ByOrderByCreatedAtDesc();
}
