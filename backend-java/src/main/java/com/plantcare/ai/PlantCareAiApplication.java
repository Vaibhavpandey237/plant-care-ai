package com.plantcare.ai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class PlantCareAiApplication {

    public static void main(String[] args) {
        System.out.println("🌿 Booting Plant Care AI System (Spring Boot + DJL Engine)...");
        SpringApplication.run(PlantCareAiApplication.class, args);
        System.out.println("✅ Plant Care AI REST API ready on http://localhost:8080/api/v1");
    }
}
