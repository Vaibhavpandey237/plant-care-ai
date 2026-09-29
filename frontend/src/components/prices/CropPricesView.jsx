import React, { useState } from 'react';
import { TrendingUp, BarChart3, MapPin } from 'lucide-react';
import { CROP_PRICES_DATABASE } from '../../data/cropPrices';

export default function CropPricesView() {
  const [selectedCropId, setSelectedCropId] = useState('wheat');
  const [selectedState, setSelectedState] = useState('All');

  const currentCropObj = CROP_PRICES_DATABASE.find(c => c.id === selectedCropId) || CROP_PRICES_DATABASE[0];

  return (
    <section className="card">
      <div className="card-title" style={{ marginBottom: '0.5rem' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <TrendingUp size={22} color="var(--accent-green)" /> Crop Prices & Government MSP Module
        </span>
      </div>
      <p className="card-subtitle">
        Official Government Minimum Support Price (MSP) in ₹ per quintal and live Mandi market rates across major agricultural hubs.
      </p>

      <div className="select-group">
        <div style={{ flex: 1 }}>
          <label style={{ fontSize: '0.85rem', fontWeight: 600, marginBottom: '0.4rem', display: 'block' }}>
            🌾 Select Crop:
          </label>
          <select 
            className="custom-select" 
            value={selectedCropId} 
            onChange={(e) => { setSelectedCropId(e.target.value); setSelectedState('All'); }}
          >
            {CROP_PRICES_DATABASE.map(crop => (
              <option key={crop.id} value={crop.id}>{crop.name} ({crop.category})</option>
            ))}
          </select>
        </div>

        <div style={{ flex: 1 }}>
          <label style={{ fontSize: '0.85rem', fontWeight: 600, marginBottom: '0.4rem', display: 'block' }}>
            📍 Filter State / Region:
          </label>
          <select 
            className="custom-select" 
            value={selectedState} 
            onChange={(e) => setSelectedState(e.target.value)}
          >
            <option value="All">All States & Mandis</option>
            {currentCropObj.states.map((st, idx) => (
              <option key={idx} value={st.stateName}>{st.stateName}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="msp-banner">
        <div>
          <span style={{ fontSize: '0.8rem', fontWeight: 800, color: 'var(--accent-teal)', textTransform: 'uppercase' }}>
            GOVERNMENT MSP RATE ({currentCropObj.mspYear})
          </span>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 700, marginTop: '0.2rem' }}>
            {currentCropObj.name}
          </h3>
        </div>
        <div style={{ textAlign: 'right' }}>
          <span className="msp-price-tag">₹{currentCropObj.mspINR.toLocaleString('en-IN')}</span>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>per quintal (100 kg)</p>
        </div>
      </div>

      <h4 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
        <BarChart3 size={18} color="var(--accent-teal)" /> Live Mandi Market Prices (₹ / Quintal)
      </h4>

      <div className="mandi-grid">
        {currentCropObj.states
          .filter(st => selectedState === 'All' || st.stateName === selectedState)
          .map(st => st.mandis.map((mandi, mIdx) => (
            <div key={mIdx} className="mandi-card">
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <h4 style={{ fontSize: '1rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                    <MapPin size={16} color="var(--accent-green)" /> {mandi.mandiName}
                  </h4>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{st.stateName}</span>
                </div>

                <div style={{ background: 'var(--input-bg)', padding: '0.75rem', borderRadius: '8px', marginBottom: '0.75rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '0.25rem' }}>
                    <span>Modal (Average) Price:</span>
                    <strong style={{ color: 'var(--accent-green)', fontSize: '1.05rem' }}>₹{mandi.modalPrice}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                    <span>Min: ₹{mandi.minPrice}</span>
                    <span>Max: ₹{mandi.maxPrice}</span>
                  </div>
                </div>

                <div style={{ fontSize: '0.8rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span>Trade vs Govt MSP:</span>
                  <span style={{ 
                    fontWeight: 700, 
                    color: mandi.modalPrice >= currentCropObj.mspINR ? '#10B981' : '#F59E0B',
                    background: mandi.modalPrice >= currentCropObj.mspINR ? 'rgba(16,185,129,0.15)' : 'rgba(245,158,11,0.15)',
                    padding: '0.2rem 0.5rem',
                    borderRadius: '6px'
                  }}>
                    {mandi.modalPrice >= currentCropObj.mspINR 
                      ? `+₹${mandi.modalPrice - currentCropObj.mspINR} Above MSP` 
                      : `-₹${currentCropObj.mspINR - mandi.modalPrice} Below MSP`}
                  </span>
                </div>
              </div>

              <div style={{ marginTop: '0.85rem', paddingTop: '0.5rem', borderTop: '1px solid var(--bg-card-border)', display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                <span>Arrivals: {mandi.arrivalQuintals} Quintals</span>
                <span>Updated: {mandi.date}</span>
              </div>
            </div>
          )))}
      </div>
    </section>
  );
}
