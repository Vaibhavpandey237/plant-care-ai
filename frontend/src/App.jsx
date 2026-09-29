import React, { useState, useEffect } from 'react';
import AuthPortal from './components/auth/AuthPortal';
import Navbar from './components/common/Navbar';
import WeatherBanner from './components/common/WeatherBanner';
import NavigationTabs from './components/common/NavigationTabs';
import DashboardView from './components/dashboard/DashboardView';
import DiagnosisView from './components/diagnosis/DiagnosisView';
import ProductsStoreView from './components/products/ProductsStoreView';
import CropPricesView from './components/prices/CropPricesView';
import GardenView from './components/garden/GardenView';
import AddPlantModal from './components/garden/AddPlantModal';
import RemindersView from './components/garden/RemindersView';
import BotanistChatView from './components/assistant/BotanistChatView';
import HistoryTrendView from './components/history/HistoryTrendView';
import AdminPanelView from './components/admin/AdminPanelView';

import { 
  INITIAL_PLANT_PROFILES, 
  INITIAL_REMINDERS, 
  WEATHER_FORECAST 
} from './data/initialPlants';
import { fetchHistory as apiFetchHistory } from './services/api';

export default function App() {
  // Theme State
  const [theme, setTheme] = useState(localStorage.getItem('plant_theme') || 'dark');

  // Auth State
  const [user, setUser] = useState(() => {
    try {
      const savedUser = localStorage.getItem('plant_user');
      const savedToken = localStorage.getItem('plant_token');
      return (savedUser && savedToken) ? JSON.parse(savedUser) : null;
    } catch (e) {
      return null;
    }
  });

  // Navigation State
  const [activeTab, setActiveTab] = useState('dashboard');
  const [moreDropdownOpen, setMoreDropdownOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // App Data State
  const [history, setHistory] = useState([]);
  const [plantProfiles, setPlantProfiles] = useState(INITIAL_PLANT_PROFILES);
  const [reminders, setReminders] = useState(INITIAL_REMINDERS);
  const [showAddPlantModal, setShowAddPlantModal] = useState(false);
  const [lastDiagnosisResult, setLastDiagnosisResult] = useState(null);

  // Sync Theme with DOM
  useEffect(() => {
    document.body.className = theme === 'light' ? 'theme-light' : 'theme-dark';
    localStorage.setItem('plant_theme', theme);
  }, [theme]);

  // Fetch History on Auth
  useEffect(() => {
    if (user) {
      loadHistory();
    }
  }, [user]);

  const loadHistory = async () => {
    try {
      const data = await apiFetchHistory();
      setHistory(data || []);
    } catch (e) {
      // Keep empty or default history if offline
    }
  };

  const toggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark');
  };

  const handleTabClick = (tabId) => {
    setActiveTab(tabId);
    setMoreDropdownOpen(false);
    setMobileMenuOpen(false);
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem('plant_token');
    localStorage.removeItem('plant_user');
  };

  const handleAddPlant = (newPlant) => {
    const createdPlant = {
      id: Date.now(),
      name: newPlant.name,
      species: newPlant.species,
      room: 'Main Room',
      healthScore: 95,
      lastWatered: 'Just now',
      status: 'Healthy'
    };
    setPlantProfiles([createdPlant, ...plantProfiles]);
  };

  const handleMarkReminderDone = (reminderId) => {
    setReminders(reminders.filter(r => r.id !== reminderId));
  };

  // 🔒 STRICT LOGIN PORTAL
  if (!user) {
    return <AuthPortal onLoginSuccess={(loggedInUser) => { setUser(loggedInUser); setActiveTab('dashboard'); }} />;
  }

  // 🔓 AUTHENTICATED APPLICATION
  return (
    <div className="app-container">
      {/* Header Navbar */}
      <Navbar
        user={user}
        theme={theme}
        toggleTheme={toggleTheme}
        onLogout={handleLogout}
        onTabClick={handleTabClick}
        mobileMenuOpen={mobileMenuOpen}
        setMobileMenuOpen={setMobileMenuOpen}
        hasResult={!!lastDiagnosisResult}
      />

      {/* Navigation Tab Bar & Drawers */}
      <NavigationTabs
        activeTab={activeTab}
        onTabClick={handleTabClick}
        user={user}
        gardenCount={plantProfiles.length}
        remindersCount={reminders.length}
        moreDropdownOpen={moreDropdownOpen}
        setMoreDropdownOpen={setMoreDropdownOpen}
        mobileMenuOpen={mobileMenuOpen}
      />

      {/* Weather Forecast Banner */}
      <WeatherBanner weatherRisk={WEATHER_FORECAST} />

      {/* TAB VIEWS */}
      {activeTab === 'dashboard' && (
        <DashboardView
          user={user}
          history={history}
          plantProfiles={plantProfiles}
          reminders={reminders}
          onTabClick={handleTabClick}
          onOpenAddPlant={() => setShowAddPlantModal(true)}
        />
      )}

      {activeTab === 'diagnose' && (
        <DiagnosisView 
          onDiagnosisComplete={(res) => {
            setLastDiagnosisResult(res);
            loadHistory();
          }} 
        />
      )}

      {activeTab === 'store' && <ProductsStoreView />}

      {activeTab === 'cropprices' && <CropPricesView />}

      {activeTab === 'garden' && (
        <GardenView 
          plantProfiles={plantProfiles} 
          onOpenAddPlant={() => setShowAddPlantModal(true)} 
        />
      )}

      {activeTab === 'reminders' && (
        <RemindersView 
          reminders={reminders} 
          onMarkDone={handleMarkReminderDone} 
        />
      )}

      {activeTab === 'chat' && <BotanistChatView />}

      {activeTab === 'history' && <HistoryTrendView history={history} />}

      {activeTab === 'admin' && <AdminPanelView />}

      {/* Add Plant Modal */}
      <AddPlantModal
        isOpen={showAddPlantModal}
        onClose={() => setShowAddPlantModal(false)}
        onAddPlant={handleAddPlant}
      />
    </div>
  );
}
