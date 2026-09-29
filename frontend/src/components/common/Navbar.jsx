import React from 'react';
import { Sprout, LogOut, Sun, Moon, Download, Menu } from 'lucide-react';

export default function Navbar({
  user,
  theme,
  toggleTheme,
  onLogout,
  onTabClick,
  mobileMenuOpen,
  setMobileMenuOpen,
  hasResult
}) {
  return (
    <header className="navbar">
      <div className="brand">
        <div className="brand-icon">
          <Sprout size={24} />
        </div>
        <div>
          <h1 className="brand-title">PlantCare AI</h1>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Enterprise Java & React Detection Platform</p>
        </div>
      </div>

      <div className="nav-actions">
        {user && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span 
              style={{ fontSize: '0.85rem', fontWeight: 600, cursor: 'pointer' }} 
              onClick={() => onTabClick('dashboard')}
            >
              {user.role === 'ADMIN' ? '👑' : '👤'} {user.name || user.username}
            </span>
            <button className="btn-icon" onClick={onLogout} title="Logout & Return to Login">
              <LogOut size={18} />
            </button>
          </div>
        )}

        <button className="btn-icon" onClick={toggleTheme} title="Toggle Theme">
          {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
        </button>

        <button className="hamburger-btn" onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
          <Menu size={20} /> Menu
        </button>

        {hasResult && (
          <button className="btn-secondary" onClick={() => window.print()}>
            <Download size={14} /> PDF
          </button>
        )}
      </div>
    </header>
  );
}
