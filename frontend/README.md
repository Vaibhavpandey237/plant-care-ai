# 🌿 PlantCare AI — Frontend (React 18 + Vite)

A modern, responsive, and performant web client for plant disease detection, crop pricing, and automated gardening care.

---

## 🚀 Tech Stack

- **Framework**: [React 18](https://react.dev/)
- **Bundler / Dev Server**: [Vite](https://vitejs.dev/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Styling**: Vanilla CSS Design System with CSS variables and light/dark theme support
- **HTTP Client**: Native Fetch API with structured service endpoints

---

## 📂 Architecture & Directory Structure

```
frontend/
├── public/
│   ├── sprout.svg             # Favicon
│   └── images/                # Plant photography
├── src/
│   ├── components/
│   │   ├── admin/             # Admin & system health dashboards
│   │   ├── assistant/         # AI Botanist conversational chat
│   │   ├── auth/              # Standalone login, registration, and reset portal
│   │   ├── common/            # Navbar, NavigationTabs, WeatherBanner
│   │   ├── dashboard/         # Personalized user summary & KPI cards
│   │   ├── diagnosis/         # Image dropzone, DJL inference & treatment viewer
│   │   ├── garden/            # Garden catalog, plant profiles & reminders
│   │   ├── history/           # Diagnosis progression trend charts
│   │   ├── prices/            # Live Mandi market pricing & Govt MSP tracker
│   │   └── products/          # Verified remedies & fertilizer store
│   ├── data/
│   │   ├── cropPrices.js      # Mandi prices & MSP rate cards
│   │   ├── initialPlants.js   # Default plant profiles & reminders
│   │   └── products.js        # Agricultural chemical & organic products dataset
│   ├── services/
│   │   └── api.js             # Centralized REST API client
│   ├── App.jsx                # Clean orchestration container
│   ├── index.css              # Theme tokens, animations & responsive grids
│   └── main.jsx               # React DOM root mounting
├── index.html                 # Entry HTML template
├── package.json               # Node dependencies & npm scripts
└── vite.config.js             # Vite configuration with proxy to backend
```

---

## 🛠️ Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Run local development server
npm run dev

# 3. Build optimized bundle for production
npm run build

# 4. Preview production build
npm run preview
```
