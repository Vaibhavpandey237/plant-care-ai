import React from 'react';
import { TrendingUp } from 'lucide-react';

export default function HistoryTrendView({ history = [] }) {
  return (
    <section className="card">
      <h2 className="card-title" style={{ marginBottom: '1rem' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <TrendingUp size={22} color="var(--accent-teal)" /> Health Score Progression Trend
        </span>
      </h2>
      <div style={{ background: 'var(--input-bg)', padding: '1.5rem', borderRadius: '12px', textAlign: 'center' }}>
        <div style={{ display: 'flex', justifyContent: 'space-around', alignItems: 'flex-end', height: '140px' }}>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <span style={{ fontSize: '0.75rem' }}>45%</span>
            <div style={{ width: '28px', height: '60px', background: '#EF4444', borderRadius: '4px', margin: '4px 0' }}></div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Scan 1</span>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <span style={{ fontSize: '0.75rem' }}>65%</span>
            <div style={{ width: '28px', height: '90px', background: '#F59E0B', borderRadius: '4px', margin: '4px 0' }}></div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Scan 2</span>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <span style={{ fontSize: '0.75rem' }}>92%</span>
            <div style={{ width: '28px', height: '130px', background: '#10B981', borderRadius: '4px', margin: '4px 0' }}></div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Scan 3</span>
          </div>
        </div>
      </div>
    </section>
  );
}
