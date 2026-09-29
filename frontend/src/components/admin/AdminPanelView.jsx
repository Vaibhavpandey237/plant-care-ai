import React from 'react';
import { ShieldCheck, Server, Database } from 'lucide-react';

export default function AdminPanelView() {
  return (
    <section className="card">
      <h2 className="card-title" style={{ marginBottom: '1rem' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <ShieldCheck size={22} color="var(--accent-green)" /> System & Database Admin Panel
        </span>
      </h2>
      <div className="admin-grid">
        <div className="admin-stat-card">
          <Server size={24} color="var(--accent-teal)" />
          <h3 style={{ fontSize: '1.25rem', marginTop: '0.5rem' }}>Java 26 / DJL</h3>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>AI Inference Engine Active</p>
        </div>
        <div className="admin-stat-card">
          <Database size={24} color="var(--accent-green)" />
          <h3 style={{ fontSize: '1.25rem', marginTop: '0.5rem' }}>MySQL DB</h3>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>`plant_care_db` Connected</p>
        </div>
      </div>
    </section>
  );
}
