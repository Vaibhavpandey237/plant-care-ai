import React from 'react';
import { Leaf, Plus } from 'lucide-react';

export default function GardenView({ plantProfiles, onOpenAddPlant }) {
  return (
    <section className="card">
      <div className="card-title">
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Leaf size={22} color="var(--accent-green)" /> My Plant Profiles Catalog
        </span>
        <button className="btn-secondary" onClick={onOpenAddPlant}>
          <Plus size={16} /> Add Plant Profile
        </button>
      </div>

      <div className="profile-grid">
        {plantProfiles.map(plant => (
          <div key={plant.id} className="profile-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <h3 style={{ fontSize: '1.05rem', fontWeight: 700 }}>{plant.name}</h3>
              <span style={{ fontSize: '0.8rem', fontWeight: 800, color: plant.healthScore > 70 ? '#10B981' : '#F59E0B' }}>
                {plant.healthScore}/100
              </span>
            </div>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Species: {plant.species} • {plant.room}</p>
            <p style={{ fontSize: '0.85rem', color: 'var(--accent-teal)', marginTop: '0.5rem' }}>Status: {plant.status}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
