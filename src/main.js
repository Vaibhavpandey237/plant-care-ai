import { INITIAL_PLANTS } from './data/plants.js';

// Global State
let plantCatalog = [...INITIAL_PLANTS];
let myGarden = JSON.parse(localStorage.getItem('flora_my_garden') || '[]');

// Default Garden pre-population if empty on first load
if (myGarden.length === 0) {
  myGarden = [
    {
      id: "monstera-deliciosa",
      name: "Monstera Deliciosa",
      image: "/images/monstera.png",
      waterFrequencyDays: 7,
      lastWatered: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toISOString(),
    },
    {
      id: "snake-plant",
      name: "Snake Plant",
      image: "/images/snake_plant.png",
      waterFrequencyDays: 14,
      lastWatered: new Date(Date.now() - 10 * 24 * 60 * 60 * 1000).toISOString(),
    }
  ];
  saveGardenState();
}

// Initialization on DOM Load
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavigation();
  renderLibrary();
  renderGarden();
  initSearchAndFilters();
  initDoctorAI();
  initCalculator();
  initModals();
  
  // Re-create icons for dynamic elements
  if (window.lucide) {
    window.lucide.createIcons();
  }
});

// Helper: Save Garden to LocalStorage
function saveGardenState() {
  localStorage.setItem('flora_my_garden', JSON.stringify(myGarden));
  updateGardenCountBadge();
}

function updateGardenCountBadge() {
  const badge = document.getElementById('garden-count');
  if (badge) badge.textContent = myGarden.length;
}

// Toast Notification
function showToast(message, type = 'info') {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `<i data-lucide="check-circle"></i> <span>${message}</span>`;
  container.appendChild(toast);
  
  if (window.lucide) window.lucide.createIcons();

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Theme Switcher
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('flora_theme') || 'dark';
  
  document.body.className = `theme-${currentTheme}`;

  toggleBtn.addEventListener('click', () => {
    const isDark = document.body.classList.contains('theme-dark');
    const newTheme = isDark ? 'light' : 'dark';
    document.body.className = `theme-${newTheme}`;
    localStorage.setItem('flora_theme', newTheme);
    showToast(`Switched to ${newTheme} mode`);
  });
}

// Navigation Tabs
function initNavigation() {
  const navBtns = document.querySelectorAll('.nav-btn');
  const panels = document.querySelectorAll('.tab-panel');

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');
      
      navBtns.forEach(b => b.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const activePanel = document.getElementById(`tab-${targetTab}`);
      if (activePanel) activePanel.classList.add('active');

      if (window.lucide) window.lucide.createIcons();
    });
  });
}

// Search & Filter System
function initSearchAndFilters() {
  const searchInput = document.getElementById('library-search');
  const clearBtn = document.getElementById('clear-search');
  const filterPills = document.querySelectorAll('.filter-pill');

  let currentCategory = 'all';
  let searchQuery = '';

  const filterCatalog = () => {
    searchQuery = searchInput.value.toLowerCase().trim();
    clearBtn.style.display = searchQuery ? 'block' : 'none';

    const filtered = plantCatalog.filter(plant => {
      const matchesSearch = plant.name.toLowerCase().includes(searchQuery) ||
                            plant.scientificName.toLowerCase().includes(searchQuery) ||
                            plant.category.toLowerCase().includes(searchQuery);

      let matchesCategory = true;
      if (currentCategory === 'indoor') matchesCategory = plant.category === 'Indoor';
      if (currentCategory === 'low-light') matchesCategory = plant.isLowLight;
      if (currentCategory === 'air-purifying') matchesCategory = plant.isAirPurifying;
      if (currentCategory === 'pet-safe') matchesCategory = plant.isPetSafe;

      return matchesSearch && matchesCategory;
    });

    renderLibrary(filtered);
  };

  searchInput.addEventListener('input', filterCatalog);
  clearBtn.addEventListener('click', () => {
    searchInput.value = '';
    filterCatalog();
  });

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentCategory = pill.getAttribute('data-filter');
      filterCatalog();
    });
  });
}

// Render Plant Library Cards
function renderLibrary(plantsToRender = plantCatalog) {
  const grid = document.getElementById('plant-grid');
  const countEl = document.getElementById('stat-total-plants');
  if (countEl) countEl.textContent = plantCatalog.length;

  if (plantsToRender.length === 0) {
    grid.innerHTML = `
      <div class="empty-state" style="grid-column: 1 / -1;">
        <div class="empty-icon"><i data-lucide="search-x"></i></div>
        <h3>No matching plants found</h3>
        <p>Try searching for a different plant species or clear filters.</p>
      </div>
    `;
    if (window.lucide) window.lucide.createIcons();
    return;
  }

  grid.innerHTML = plantsToRender.map(plant => `
    <div class="plant-card" data-id="${plant.id}">
      <div class="plant-card-img-wrapper">
        <img src="${plant.image}" alt="${plant.name}" class="plant-card-img" />
        <span class="plant-badge-top">${plant.difficulty}</span>
      </div>
      <div class="plant-card-content">
        <h3 class="plant-title">${plant.name}</h3>
        <span class="plant-scientific">${plant.scientificName}</span>
        <div class="plant-specs">
          <div class="spec-item">
            <i data-lucide="sun"></i> <span>${plant.light.split(' ')[0]}</span>
          </div>
          <div class="spec-item">
            <i data-lucide="droplet"></i> <span>${plant.waterFrequencyDays}d</span>
          </div>
          <div class="spec-item">
            <i data-lucide="shield"></i> <span>${plant.isPetSafe ? 'Pet Safe' : 'Toxic'}</span>
          </div>
        </div>
      </div>
    </div>
  `).join('');

  // Add click handlers for detail modal
  grid.querySelectorAll('.plant-card').forEach(card => {
    card.addEventListener('click', () => {
      const id = card.getAttribute('data-id');
      openPlantModal(id);
    });
  });

  if (window.lucide) window.lucide.createIcons();
}

// Render My Garden Cards
function renderGarden() {
  const grid = document.getElementById('garden-grid');
  const emptyState = document.getElementById('garden-empty-state');
  updateGardenCountBadge();

  if (myGarden.length === 0) {
    grid.style.display = 'none';
    emptyState.style.display = 'flex';
    return;
  }

  grid.style.display = 'grid';
  emptyState.style.display = 'none';

  grid.innerHTML = myGarden.map((item, index) => {
    const lastWateredDate = new Date(item.lastWatered);
    const daysSinceWatered = Math.floor((Date.now() - lastWateredDate.getTime()) / (1000 * 60 * 60 * 24));
    const daysUntilNext = item.waterFrequencyDays - daysSinceWatered;
    const progressPercent = Math.max(0, Math.min(100, (daysSinceWatered / item.waterFrequencyDays) * 100));

    let statusText = `Water in ${daysUntilNext} day(s)`;
    if (daysUntilNext <= 0) statusText = `🚨 Needs Water Today!`;

    return `
      <div class="garden-card">
        <img src="${item.image || '/images/monstera.png'}" alt="${item.name}" class="garden-thumb" />
        <div class="garden-info">
          <h4 class="garden-name">${item.name}</h4>
          <div class="garden-schedule">${statusText}</div>
          <div class="progress-bar-container">
            <div class="progress-fill" style="width: ${progressPercent}%;"></div>
          </div>
          <button class="water-action-btn" data-index="${index}">
            <i data-lucide="droplet"></i> Water Now
          </button>
        </div>
      </div>
    `;
  }).join('');

  // Attach Water Event Listeners
  grid.querySelectorAll('.water-action-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const index = parseInt(btn.getAttribute('data-index'), 10);
      waterGardenPlant(index);
    });
  });

  // Attach Water All Listener
  const waterAllBtn = document.getElementById('btn-water-all');
  if (waterAllBtn) {
    waterAllBtn.onclick = () => {
      myGarden.forEach(plant => {
        plant.lastWatered = new Date().toISOString();
      });
      saveGardenState();
      renderGarden();
      showToast('💦 All plants in your garden have been watered!');
    };
  }

  if (window.lucide) window.lucide.createIcons();
}

function waterGardenPlant(index) {
  if (myGarden[index]) {
    myGarden[index].lastWatered = new Date().toISOString();
    saveGardenState();
    renderGarden();
    showToast(`💦 ${myGarden[index].name} has been refreshed!`);
  }
}

// Plant Details Modal
function openPlantModal(plantId) {
  const plant = plantCatalog.find(p => p.id === plantId);
  if (!plant) return;

  const modal = document.getElementById('plant-modal');
  const modalContent = document.getElementById('modal-content');

  modalContent.innerHTML = `
    <div class="modal-plant-hero">
      <img src="${plant.image}" alt="${plant.name}" />
      <div class="modal-plant-hero-overlay">
        <h2>${plant.name}</h2>
        <span style="color: var(--text-muted); font-style: italic;">${plant.scientificName}</span>
      </div>
    </div>
    <div class="modal-plant-body">
      <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 1rem;">${plant.description}</p>
      
      <div class="modal-grid-stats">
        <div class="modal-stat-box">
          <i data-lucide="sun" style="color: var(--sun-gold)"></i>
          <div style="font-size: 0.8rem; margin-top: 0.3rem;">${plant.light}</div>
        </div>
        <div class="modal-stat-box">
          <i data-lucide="droplet" style="color: var(--water-blue)"></i>
          <div style="font-size: 0.8rem; margin-top: 0.3rem;">Every ${plant.waterFrequencyDays} days</div>
        </div>
        <div class="modal-stat-box">
          <i data-lucide="thermometer" style="color: var(--accent-light)"></i>
          <div style="font-size: 0.8rem; margin-top: 0.3rem;">${plant.temperature}</div>
        </div>
      </div>

      <h4 style="margin: 1.25rem 0 0.5rem 0; color: var(--accent-light);"><i data-lucide="sparkles"></i> Pro Care Tips</h4>
      <ul style="padding-left: 1.25rem; color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">
        ${plant.careTips.map(tip => `<li style="margin-bottom: 0.4rem;">${tip}</li>`).join('')}
      </ul>

      <div style="margin-top: 1.5rem; text-align: right;">
        <button class="btn btn-primary" id="btn-modal-add-garden">
          <i data-lucide="plus"></i> Add to My Garden
        </button>
      </div>
    </div>
  `;

  modal.classList.add('active');
  if (window.lucide) window.lucide.createIcons();

  document.getElementById('btn-modal-add-garden').onclick = () => {
    const exists = myGarden.some(g => g.name === plant.name);
    if (!exists) {
      myGarden.push({
        id: plant.id,
        name: plant.name,
        image: plant.image,
        waterFrequencyDays: plant.waterFrequencyDays,
        lastWatered: new Date().toISOString()
      });
      saveGardenState();
      renderGarden();
      showToast(`🌱 Added ${plant.name} to My Garden!`);
    } else {
      showToast(`${plant.name} is already in your garden!`, 'info');
    }
    modal.classList.remove('active');
  };
}

// Plant Doctor AI Diagnostic Logic
function initDoctorAI() {
  const btnDiagnose = document.getElementById('btn-diagnose');
  const resultCard = document.getElementById('doctor-result');

  btnDiagnose.addEventListener('click', () => {
    const selectedSymptoms = Array.from(document.querySelectorAll('#symptoms-list input:checked')).map(i => i.value);

    if (selectedSymptoms.length === 0) {
      showToast('Please select at least one symptom to diagnose!', 'info');
      return;
    }

    // AI Diagnosis synthesis
    let issueTitle = "Overwatering / Soil Drainage Issue";
    let severity = "Moderate Severity";
    let steps = [
      "Allow the top 2-3 inches of soil to dry out completely before watering again.",
      "Ensure the plant pot has drainage holes at the bottom.",
      "Check root system for brown, soft roots; prune rot with sterile scissors."
    ];

    if (selectedSymptoms.includes('brown_tips')) {
      issueTitle = "Low Relative Humidity / Dry Air Burn";
      severity = "Mild Issue";
      steps = [
        "Increase humidity using a pebble tray with water under the pot.",
        "Group humidity-loving plants together to create a microclimate.",
        "Avoid keeping plant directly next to HVAC air conditioning vents."
      ];
    } else if (selectedSymptoms.includes('white_webs')) {
      issueTitle = "Spider Mite or Mealybug Infestation";
      severity = "High Priority";
      steps = [
        "Isolate plant immediately from other indoor plants.",
        "Wipe leaves down thoroughly with organic Neem Oil spray or insecticidal soap.",
        "Repeat leaf treatment every 5 days for 3 consecutive weeks."
      ];
    } else if (selectedSymptoms.includes('root_rot')) {
      issueTitle = "Severe Root Rot (Pythium / Phytophthora)";
      severity = "Critical Risk";
      steps = [
        "Remove plant from pot and gently wash excess wet soil off roots.",
        "Trim all black mushy roots back to healthy firm white tissue.",
        "Repot in fresh sterile well-draining soil mix with extra perlite."
      ];
    }

    resultCard.innerHTML = `
      <div class="diagnosis-result-content">
        <span class="diagnosis-tag">${severity}</span>
        <h3>${issueTitle}</h3>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.95rem;">
          Based on selected symptoms, here is your step-by-step treatment protocol:
        </p>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${steps.map((step, idx) => `
            <div class="remedy-step">
              <span class="step-num">${idx + 1}</span>
              <span style="font-size: 0.9rem; line-height: 1.5;">${step}</span>
            </div>
          `).join('')}
        </div>

        <button class="btn btn-secondary btn-block" style="margin-top: 1.5rem;" id="btn-reset-doctor">
          <i data-lucide="refresh-cw"></i> Diagnose Another Plant
        </button>
      </div>
    `;

    if (window.lucide) window.lucide.createIcons();

    document.getElementById('btn-reset-doctor').onclick = () => {
      document.querySelectorAll('#symptoms-list input').forEach(c => c.checked = false);
      resultCard.innerHTML = `
        <div class="initial-doctor-state">
          <i data-lucide="heart-pulse" class="doctor-placeholder-icon"></i>
          <h3>Ready to Diagnose</h3>
          <p>Select one or more symptoms on the left and hit <strong>Run AI Diagnosis</strong> for personalized care instructions.</p>
        </div>
      `;
      if (window.lucide) window.lucide.createIcons();
    };
  });
}

// Environmental Care Calculator
function initCalculator() {
  const potSelect = document.getElementById('calc-pot-type');
  const lightSelect = document.getElementById('calc-light');
  const tempSlider = document.getElementById('calc-temp');
  const humiditySlider = document.getElementById('calc-humidity');

  const valTemp = document.getElementById('val-temp');
  const valHumidity = document.getElementById('val-humidity');
  const resWaterFreq = document.getElementById('res-water-freq');
  const resSunAdvice = document.getElementById('res-sun-advice');
  const resHumidityAdvice = document.getElementById('res-humidity-advice');

  const recalculate = () => {
    const temp = parseInt(tempSlider.value, 10);
    const humidity = parseInt(humiditySlider.value, 10);
    const pot = potSelect.value;
    const light = lightSelect.value;

    valTemp.textContent = `${temp}°C`;
    valHumidity.textContent = `${humidity}%`;

    let baseDays = 7;

    // Adjust for temp
    if (temp > 26) baseDays -= 2;
    else if (temp < 18) baseDays += 3;

    // Adjust for humidity
    if (humidity < 40) baseDays -= 1;
    else if (humidity > 65) baseDays += 2;

    // Adjust for pot material
    if (pot === 'terracotta') baseDays -= 2;
    if (pot === 'fabric') baseDays -= 3;

    // Adjust for light
    if (light === 'bright-direct') baseDays -= 2;
    if (light === 'low-light') baseDays += 4;

    const finalDays = Math.max(2, baseDays);
    resWaterFreq.textContent = `Every ${finalDays} Days`;

    if (light === 'bright-direct') {
      resSunAdvice.textContent = "High light intensity accelerates transpiration. Watch for sun scorched foliage.";
    } else if (light === 'low-light') {
      resSunAdvice.textContent = "Low light slows growth and water uptake. Water infrequently to prevent root sogginess.";
    } else {
      resSunAdvice.textContent = "Ideal bright indirect window exposure. Rotate pot 90° weekly for symmetrical growth.";
    }

    if (humidity < 40) {
      resHumidityAdvice.textContent = "Air is dry! Use a humidifier or mist regularly to prevent crispy brown tips.";
    } else {
      resHumidityAdvice.textContent = "Optimal tropical humidity level. Keeps leaves lush and vibrant.";
    }
  };

  [potSelect, lightSelect, tempSlider, humiditySlider].forEach(el => {
    el.addEventListener('input', recalculate);
  });
}

// Modals Management
function initModals() {
  const modal = document.getElementById('plant-modal');
  const addModal = document.getElementById('add-plant-modal');

  document.getElementById('modal-close').onclick = () => modal.classList.remove('active');
  document.getElementById('add-modal-close').onclick = () => addModal.classList.remove('active');
  document.getElementById('add-modal-cancel').onclick = () => addModal.classList.remove('active');

  document.getElementById('btn-add-plant').onclick = () => {
    addModal.classList.add('active');
  };

  // Add Custom Plant Form Submission
  const addForm = document.getElementById('form-add-plant');
  addForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('add-name').value;
    const scientific = document.getElementById('add-scientific').value || 'Houseplant';
    const category = document.getElementById('add-category').value;
    const waterDays = parseInt(document.getElementById('add-water-days').value, 10) || 7;
    const light = document.getElementById('add-light').value;

    const newPlant = {
      id: `custom-${Date.now()}`,
      name,
      scientificName: scientific,
      category,
      image: "/images/monstera.png",
      waterFrequencyDays: waterDays,
      light,
      humidity: "50-60%",
      temperature: "20-25°C",
      toxicity: "Unknown",
      isPetSafe: true,
      isLowLight: light === 'Low Light',
      isAirPurifying: true,
      difficulty: "Easy",
      description: "Custom user-added houseplant.",
      careTips: ["Water regularly based on soil dampness.", "Provide recommended sunlight."]
    };

    plantCatalog.unshift(newPlant);
    renderLibrary();

    myGarden.push({
      id: newPlant.id,
      name: newPlant.name,
      image: newPlant.image,
      waterFrequencyDays: waterDays,
      lastWatered: new Date().toISOString()
    });
    saveGardenState();
    renderGarden();

    addModal.classList.remove('active');
    addForm.reset();
    showToast(`🎉 Added ${name} to your Plant Collection!`);
  });
}
