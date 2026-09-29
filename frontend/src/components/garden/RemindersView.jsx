import React from 'react';
import { Bell, CheckCircle2 } from 'lucide-react';

export default function RemindersView({ reminders, onMarkDone }) {
  return (
    <section className="card">
      <h2 className="card-title" style={{ marginBottom: '1rem' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Bell size={22} color="var(--accent-teal)" /> Care & Watering Reminders
        </span>
      </h2>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
        {reminders.length === 0 ? (
          <p style={{ textAlign: 'center', color: 'var(--text-muted)', padding: '2rem 0' }}>
            🎉 All caught up! No pending reminders.
          </p>
        ) : (
          reminders.map(rem => (
            <div key={rem.id} className="rec-item" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h4 style={{ fontSize: '0.95rem' }}>{rem.plant} — {rem.task}</h4>
                <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Due: {rem.dueDate}</p>
              </div>
              <button className="btn-secondary" onClick={() => onMarkDone(rem.id)}>
                <CheckCircle2 size={16} /> Mark Done
              </button>
            </div>
          ))
        )}
      </div>
    </section>
  );
}
