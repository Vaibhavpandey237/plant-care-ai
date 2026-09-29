import React from 'react';
import { CloudSun } from 'lucide-react';

export default function WeatherBanner({ weatherRisk }) {
  if (!weatherRisk) return null;

  return (
    <div className="weather-banner">
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.85rem' }}>
        <CloudSun size={28} color="var(--accent-teal)" />
        <div>
          <h3 style={{ fontSize: '0.95rem', fontWeight: 700 }}>🌦️ Weather Disease Risk Forecast</h3>
          <p style={{ fontSize: '0.82rem', color: 'var(--text-muted)' }}>
            {weatherRisk.city} • Temp: {weatherRisk.temp} • Humidity: {weatherRisk.humidity}
          </p>
        </div>
      </div>
      <div style={{ textAlign: 'right' }}>
        <span style={{ 
          fontSize: '0.75rem', 
          fontWeight: 800, 
          padding: '0.25rem 0.6rem', 
          borderRadius: '12px', 
          background: 'rgba(239, 68, 68, 0.2)', 
          color: '#EF4444' 
        }}>
          {weatherRisk.riskLevel}
        </span>
        <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '0.2rem' }}>
          {weatherRisk.advice}
        </p>
      </div>
    </div>
  );
}
