import React from 'react';
import { 
  LayoutDashboard, Activity, ShoppingCart, TrendingUp, Leaf, 
  ChevronDown, ChevronUp, MessageSquare, History, Bell, ShieldCheck 
} from 'lucide-react';

export default function NavigationTabs({
  activeTab,
  onTabClick,
  user,
  gardenCount,
  remindersCount,
  moreDropdownOpen,
  setMoreDropdownOpen,
  mobileMenuOpen
}) {
  const isMoreTabActive = ['chat', 'history', 'reminders', 'admin'].includes(activeTab);

  return (
    <>
      {/* MOBILE NAVIGATION DRAWER */}
      {mobileMenuOpen && (
        <nav className="mobile-nav-drawer">
          <button className={`tab-btn ${activeTab === 'dashboard' ? 'active' : ''}`} onClick={() => onTabClick('dashboard')}>
            <LayoutDashboard size={18} /> My Dashboard
          </button>
          <button className={`tab-btn ${activeTab === 'diagnose' ? 'active' : ''}`} onClick={() => onTabClick('diagnose')}>
            <Activity size={18} /> AI Diagnosis
          </button>
          <button className={`tab-btn ${activeTab === 'store' ? 'active' : ''}`} onClick={() => onTabClick('store')}>
            <ShoppingCart size={18} /> Products & Remedies
          </button>
          <button className={`tab-btn ${activeTab === 'cropprices' ? 'active' : ''}`} onClick={() => onTabClick('cropprices')}>
            <TrendingUp size={18} /> Crop Prices & MSP
          </button>
          <button className={`tab-btn ${activeTab === 'garden' ? 'active' : ''}`} onClick={() => onTabClick('garden')}>
            <Leaf size={18} /> My Garden ({gardenCount})
          </button>
          <button className={`tab-btn ${activeTab === 'chat' ? 'active' : ''}`} onClick={() => onTabClick('chat')}>
            <MessageSquare size={18} /> AI Botanist Chat
          </button>
          <button className={`tab-btn ${activeTab === 'history' ? 'active' : ''}`} onClick={() => onTabClick('history')}>
            <History size={18} /> History Graph
          </button>
          <button className={`tab-btn ${activeTab === 'reminders' ? 'active' : ''}`} onClick={() => onTabClick('reminders')}>
            <Bell size={18} /> Reminders ({remindersCount})
          </button>
          {user?.role === 'ADMIN' && (
            <button className={`tab-btn ${activeTab === 'admin' ? 'active' : ''}`} onClick={() => onTabClick('admin')}>
              <ShieldCheck size={18} /> Admin Panel
            </button>
          )}
        </nav>
      )}

      {/* DESKTOP NAVIGATION TAB BAR */}
      <nav className="tab-bar">
        <div className="tab-btn-group">
          <button className={`tab-btn ${activeTab === 'dashboard' ? 'active' : ''}`} onClick={() => onTabClick('dashboard')}>
            <LayoutDashboard size={18} /> My Dashboard
          </button>
          <button className={`tab-btn ${activeTab === 'diagnose' ? 'active' : ''}`} onClick={() => onTabClick('diagnose')}>
            <Activity size={18} /> AI Diagnosis
          </button>
          <button className={`tab-btn ${activeTab === 'store' ? 'active' : ''}`} onClick={() => onTabClick('store')}>
            <ShoppingCart size={18} /> Products & Remedies
          </button>
          <button className={`tab-btn ${activeTab === 'cropprices' ? 'active' : ''}`} onClick={() => onTabClick('cropprices')}>
            <TrendingUp size={18} /> Crop Prices & MSP
          </button>
          <button className={`tab-btn ${activeTab === 'garden' ? 'active' : ''}`} onClick={() => onTabClick('garden')}>
            <Leaf size={18} /> My Garden ({gardenCount})
          </button>
        </div>

        {/* MORE ▾ DROPDOWN MENU */}
        <div className="more-dropdown-container">
          <button 
            className={`tab-btn ${isMoreTabActive ? 'active' : ''}`} 
            onClick={() => setMoreDropdownOpen(!moreDropdownOpen)}
          >
            More {moreDropdownOpen ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          </button>

          {moreDropdownOpen && (
            <div className="more-dropdown-menu">
              <button className={`dropdown-item ${activeTab === 'chat' ? 'active' : ''}`} onClick={() => onTabClick('chat')}>
                <MessageSquare size={16} /> AI Botanist Chat
              </button>
              <button className={`dropdown-item ${activeTab === 'history' ? 'active' : ''}`} onClick={() => onTabClick('history')}>
                <History size={16} /> History Graph
              </button>
              <button className={`dropdown-item ${activeTab === 'reminders' ? 'active' : ''}`} onClick={() => onTabClick('reminders')}>
                <Bell size={16} /> Reminders ({remindersCount})
              </button>
              {user?.role === 'ADMIN' && (
                <button className={`dropdown-item ${activeTab === 'admin' ? 'active' : ''}`} onClick={() => onTabClick('admin')}>
                  <ShieldCheck size={16} /> Admin Panel
                </button>
              )}
            </div>
          )}
        </div>
      </nav>
    </>
  );
}
