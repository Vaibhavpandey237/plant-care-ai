package com.plantcare.ai.service;

import org.springframework.stereotype.Service;
import javax.imageio.ImageIO;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Service
public class ImageProcessingService {

    /**
     * Reads image byte array into a Java BufferedImage.
     */
    public BufferedImage readImage(byte[] imageBytes) throws IOException {
        ByteArrayInputStream bais = new ByteArrayInputStream(imageBytes);
        BufferedImage image = ImageIO.read(bais);
        if (image == null) {
            throw new IOException("Unsupported image format or corrupt byte stream.");
        }
        return image;
    }

    /**
     * Resizes a BufferedImage to target dimensions (e.g. 224x224 for DJL tensor input).
     */
    public BufferedImage resizeImage(BufferedImage originalImage, int targetWidth, int targetHeight) {
        BufferedImage resizedImage = new BufferedImage(targetWidth, targetHeight, BufferedImage.TYPE_INT_RGB);
        Graphics2D g2d = resizedImage.createGraphics();
        g2d.drawImage(originalImage, 0, 0, targetWidth, targetHeight, null);
        g2d.dispose();
        return resizedImage;
    }

    /**
     * Analyzes leaf pixel color histograms to calculate chlorosis (yellowing)
     * and necrosis (browning) percentages across the foliage.
     */
    public Map<String, Object> analyzeLeafColorMetrics(BufferedImage image) {
        int width = image.getWidth();
        int height = image.getHeight();
        long totalPixels = (long) width * height;
        
        long yellowPixels = 0;
        long brownPixels = 0;
        long greenPixels = 0;

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int rgb = image.getRGB(x, y);
                int r = (rgb >> 16) & 0xFF;
                int g = (rgb >> 8) & 0xFF;
                int b = rgb & 0xFF;

                // Green detection (Chlorophyll)
                if (g > r + 10 && g > b + 10) {
                    greenPixels++;
                }
                // Yellow detection (Chlorosis)
                else if (r > 130 && g > 130 && b < 110) {
                    yellowPixels++;
                }
                // Brown detection (Necrosis / Drying)
                else if (r > 100 && g > 60 && g < r && b < 70) {
                    brownPixels++;
                }
            }
        }

        double greenPct = (greenPixels * 100.0) / Math.max(1, totalPixels);
        double yellowPct = (yellowPixels * 100.0) / Math.max(1, totalPixels);
        double brownPct = (brownPixels * 100.0) / Math.max(1, totalPixels);

        Map<String, Object> metrics = new HashMap<>();
        metrics.put("imageWidth", width);
        metrics.put("imageHeight", height);
        metrics.put("greenCoveragePct", Math.round(greenPct * 100.0) / 100.0);
        metrics.put("chlorosisYellowPct", Math.round(yellowPct * 100.0) / 100.0);
        metrics.put("necrosisBrownPct", Math.round(brownPct * 100.0) / 100.0);

        return metrics;
    }
}
