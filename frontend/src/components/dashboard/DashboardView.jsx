import React from 'react';
import { Activity, MessageSquare, Plus, Bell, Download } from 'lucide-react';

export default function DashboardView({
  user,
  history,
  plantProfiles,
  reminders,
  onTabClick,
  onOpenAddPlant
}) {
  return (
    <main style={{ display: 'flex', flexDirection: 'column', gap: '1.75rem' }}>
      {/* Welcome Banner */}
      <section className="card" style={{ background: 'linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(20, 184, 166, 0.15))' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
          <div>
            <h2 style={{ fontSize: '1.4rem', fontWeight: 800 }}>Welcome back, {user.name || user.username}! 👋</h2>
            <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
              Here is your plant health summary, garden overview, and active care recommendations.
            </p>
          </div>
          <button className="btn-primary" style={{ width: 'auto', margin: 0 }} onClick={() => onTabClick('diagnose')}>
            <Activity size={18} /> Diagnose New Leaf
          </button>
        </div>
      </section>

      {/* KPI Stats Grid */}
      <section className="profile-grid">
        <div className="profile-card">
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>TOTAL DIAGNOSES</span>
          <h3 style={{ fontSize: '1.6rem', fontWeight: 800, marginTop: '0.5rem' }}>{history.length || 3}</h3>
        </div>
        <div className="profile-card">
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>HEALTHY PLANTS</span>
          <h3 style={{ fontSize: '1.6rem', fontWeight: 800, marginTop: '0.5rem', color: '#10B981' }}>
            {plantProfiles.filter(p => p.healthScore >= 70).length} / {plantProfiles.length}
          </h3>
        </div>
        <div className="profile-card">
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>NEEDS ATTENTION</span>
          <h3 style={{ fontSize: '1.6rem', fontWeight: 800, marginTop: '0.5rem', color: '#F59E0B' }}>
            {plantProfiles.filter(p => p.healthScore < 70).length}
          </h3>
        </div>
        <div className="profile-card">
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>PENDING REMINDERS</span>
          <h3 style={{ fontSize: '1.6rem', fontWeight: 800, marginTop: '0.5rem' }}>{reminders.length}</h3>
        </div>
      </section>

      {/* Quick Actions Shortcuts */}
      <section className="card">
        <h3 className="card-title" style={{ fontSize: '1.1rem', marginBottom: '1rem' }}>
          ⚡ Quick Actions Shortcuts
        </h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
          <button className="btn-secondary" style={{ padding: '0.85rem', justifyContent: 'center' }} onClick={() => onTabClick('diagnose')}>
            <Activity size={18} color="var(--accent-green)" /> Diagnose New Leaf
          </button>
          <button className="btn-secondary" style={{ padding: '0.85rem', justifyContent: 'center' }} onClick={() => onTabClick('chat')}>
            <MessageSquare size={18} color="var(--accent-teal)" /> Ask AI Botanist
          </button>
          <button className="btn-secondary" style={{ padding: '0.85rem', justifyContent: 'center' }} onClick={onOpenAddPlant}>
            <Plus size={18} color="#10B981" /> Add New Plant
          </button>
          <button className="btn-secondary" style={{ padding: '0.85rem', justifyContent: 'center' }} onClick={() => onTabClick('reminders')}>
            <Bell size={18} color="#F59E0B" /> Check Reminders
          </button>
        </div>
      </section>

      {/* Recent AI Diagnoses Table */}
      <section className="card">
        <h3 className="card-title" style={{ fontSize: '1.1rem', marginBottom: '1rem' }}>
          📜 Your Recent AI Diagnoses & Reports
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
          <div className="rec-item" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <h4 style={{ fontSize: '0.95rem' }}>Potato → Early Blight</h4>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Scan: leaf_photo_01.jpg • Score: 45/100 • Severity: MODERATE</p>
            </div>
            <button className="btn-secondary" onClick={() => window.print()}>
              <Download size={14} /> Download PDF
            </button>
          </div>

          <div className="rec-item" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <h4 style={{ fontSize: '0.95rem' }}>Bell Pepper → Healthy</h4>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Scan: pepper_leaf.jpg • Score: 95/100 • Severity: LOW</p>
            </div>
            <button className="btn-secondary" onClick={() => window.print()}>
              <Download size={14} /> Download PDF
            </button>
          </div>
        </div>
      </section>
    </main>
  );
}
