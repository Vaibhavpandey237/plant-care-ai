var e=(e,t,n)=>()=>{if(n)throw n[0];try{return e&&(t=e(e=0)),t}catch(e){throw n=[e],e}},t=(e,t)=>()=>(t||(e((t={exports:{}}).exports,t),e=null),t.exports);(function(){let e=document.createElement(`link`).relList;if(e&&e.supports&&e.supports(`modulepreload`))return;for(let e of document.querySelectorAll(`link[rel="modulepreload"]`))n(e);new MutationObserver(e=>{for(let t of e)if(t.type===`childList`)for(let e of t.addedNodes)e.tagName===`LINK`&&e.rel===`modulepreload`&&n(e)}).observe(document,{childList:!0,subtree:!0});function t(e){let t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),t.credentials=e.crossOrigin===`use-credentials`?`include`:e.crossOrigin===`anonymous`?`omit`:`same-origin`,t}function n(e){if(e.ep)return;e.ep=!0;let n=t(e);fetch(e.href,n)}})();var n,r=e((()=>{n=[{id:`monstera-deliciosa`,name:`Monstera Deliciosa`,scientificName:`Monstera deliciosa`,category:`Indoor`,image:`/images/monstera.png`,waterFrequencyDays:7,light:`Bright Indirect`,humidity:`60-80%`,temperature:`18-30°C`,toxicity:`Toxic to Pets 🐾`,isPetSafe:!1,isLowLight:!1,isAirPurifying:!0,difficulty:`Easy`,description:`Iconic tropical plant famous for its large, glossy leaves featuring beautiful natural split patterns (fenestrations). Native to the tropical forests of Central America.`,careTips:[`Wipe leaves with a damp cloth monthly to remove dust.`,`Provide a moss pole or trellis for support as it grows climbing aerial roots.`,`Water thoroughly when top 2 inches of soil feel completely dry.`]},{id:`snake-plant`,name:`Snake Plant (Sansevieria)`,scientificName:`Sansevieria trifasciata`,category:`Air Purifying`,image:`/images/snake_plant.png`,waterFrequencyDays:14,light:`Low to Bright Indirect`,humidity:`30-50%`,temperature:`15-29°C`,toxicity:`Mildly Toxic to Pets 🐾`,isPetSafe:!1,isLowLight:!0,isAirPurifying:!0,difficulty:`Beginner`,description:`Extremely resilient architectural plant with stiff, upright sword-like leaves. Outstanding oxygen producer and bedroom air purifier.`,careTips:[`Tolerates neglect very well. Better to underwater than overwater.`,`Use well-draining cactus or succulent soil mix.`,`Can thrive in low-light corners and windowless offices.`]},{id:`peace-lily`,name:`Peace Lily`,scientificName:`Spathiphyllum wallisii`,category:`Flowering`,image:`/images/peace_lily.png`,waterFrequencyDays:5,light:`Medium Indirect`,humidity:`50-70%`,temperature:`18-26°C`,toxicity:`Toxic to Cats & Dogs 🐾`,isPetSafe:!1,isLowLight:!0,isAirPurifying:!0,difficulty:`Easy`,description:`Lush dark green foliage that blooms elegant white spathes. Known for dramatically drooping when thirsty and rebounding within hours after watering.`,careTips:[`Keep soil consistently moist but never waterlogged.`,`Prune spent white flowers at the base of the stem.`,`Mist leaves or place near a humidifier to keep leaf tips crisp and green.`]},{id:`calathea-orbifolia`,name:`Calathea Orbifolia`,scientificName:`Goeppertia orbifolia`,category:`Indoor`,image:`/images/calathea.png`,waterFrequencyDays:6,light:`Medium Indirect`,humidity:`65-80%`,temperature:`18-24°C`,toxicity:`Pet Safe 🐶🐱`,isPetSafe:!0,isLowLight:!1,isAirPurifying:!0,difficulty:`Intermediate`,description:`Breathtaking prayer plant with enormous, round leaves displaying metallic silver stripes. Folds its leaves upward at night like praying hands.`,careTips:[`Use filtered, distilled, or rainwater to avoid mineral leaf burn.`,`Keep humidity high (60%+); avoid placement near heating vents or drafty windows.`,`Never allow soil to dry out completely.`]}]}));t((()=>{r();var e=[...n],t=JSON.parse(localStorage.getItem(`flora_my_garden`)||`[]`);t.length===0&&(t=[{id:`monstera-deliciosa`,name:`Monstera Deliciosa`,image:`/images/monstera.png`,waterFrequencyDays:7,lastWatered:new Date(Date.now()-2592e5).toISOString()},{id:`snake-plant`,name:`Snake Plant`,image:`/images/snake_plant.png`,waterFrequencyDays:14,lastWatered:new Date(Date.now()-864e6).toISOString()}],i()),document.addEventListener(`DOMContentLoaded`,()=>{s(),c(),u(),d(),l(),m(),h(),g(),window.lucide&&window.lucide.createIcons()});function i(){localStorage.setItem(`flora_my_garden`,JSON.stringify(t)),a()}function a(){let e=document.getElementById(`garden-count`);e&&(e.textContent=t.length)}function o(e,t=`info`){let n=document.getElementById(`toast-container`),r=document.createElement(`div`);r.className=`toast toast-${t}`,r.innerHTML=`<i data-lucide="check-circle"></i> <span>${e}</span>`,n.appendChild(r),window.lucide&&window.lucide.createIcons(),setTimeout(()=>{r.style.opacity=`0`,r.style.transform=`translateX(100%)`,setTimeout(()=>r.remove(),300)},3500)}function s(){let e=document.getElementById(`theme-toggle`),t=localStorage.getItem(`flora_theme`)||`dark`;document.body.className=`theme-${t}`,e.addEventListener(`click`,()=>{let e=document.body.classList.contains(`theme-dark`)?`light`:`dark`;document.body.className=`theme-${e}`,localStorage.setItem(`flora_theme`,e),o(`Switched to ${e} mode`)})}function c(){let e=document.querySelectorAll(`.nav-btn`),t=document.querySelectorAll(`.tab-panel`);e.forEach(n=>{n.addEventListener(`click`,()=>{let r=n.getAttribute(`data-tab`);e.forEach(e=>e.classList.remove(`active`)),t.forEach(e=>e.classList.remove(`active`)),n.classList.add(`active`);let i=document.getElementById(`tab-${r}`);i&&i.classList.add(`active`),window.lucide&&window.lucide.createIcons()})})}function l(){let t=document.getElementById(`library-search`),n=document.getElementById(`clear-search`),r=document.querySelectorAll(`.filter-pill`),i=`all`,a=``,o=()=>{a=t.value.toLowerCase().trim(),n.style.display=a?`block`:`none`,u(e.filter(e=>{let t=e.name.toLowerCase().includes(a)||e.scientificName.toLowerCase().includes(a)||e.category.toLowerCase().includes(a),n=!0;return i===`indoor`&&(n=e.category===`Indoor`),i===`low-light`&&(n=e.isLowLight),i===`air-purifying`&&(n=e.isAirPurifying),i===`pet-safe`&&(n=e.isPetSafe),t&&n}))};t.addEventListener(`input`,o),n.addEventListener(`click`,()=>{t.value=``,o()}),r.forEach(e=>{e.addEventListener(`click`,()=>{r.forEach(e=>e.classList.remove(`active`)),e.classList.add(`active`),i=e.getAttribute(`data-filter`),o()})})}function u(t=e){let n=document.getElementById(`plant-grid`),r=document.getElementById(`stat-total-plants`);if(r&&(r.textContent=e.length),t.length===0){n.innerHTML=`
      <div class="empty-state" style="grid-column: 1 / -1;">
        <div class="empty-icon"><i data-lucide="search-x"></i></div>
        <h3>No matching plants found</h3>
        <p>Try searching for a different plant species or clear filters.</p>
      </div>
    `,window.lucide&&window.lucide.createIcons();return}n.innerHTML=t.map(e=>`
    <div class="plant-card" data-id="${e.id}">
      <div class="plant-card-img-wrapper">
        <img src="${e.image}" alt="${e.name}" class="plant-card-img" />
        <span class="plant-badge-top">${e.difficulty}</span>
      </div>
      <div class="plant-card-content">
        <h3 class="plant-title">${e.name}</h3>
        <span class="plant-scientific">${e.scientificName}</span>
        <div class="plant-specs">
          <div class="spec-item">
            <i data-lucide="sun"></i> <span>${e.light.split(` `)[0]}</span>
          </div>
          <div class="spec-item">
            <i data-lucide="droplet"></i> <span>${e.waterFrequencyDays}d</span>
          </div>
          <div class="spec-item">
            <i data-lucide="shield"></i> <span>${e.isPetSafe?`Pet Safe`:`Toxic`}</span>
          </div>
        </div>
      </div>
    </div>
  `).join(``),n.querySelectorAll(`.plant-card`).forEach(e=>{e.addEventListener(`click`,()=>{p(e.getAttribute(`data-id`))})}),window.lucide&&window.lucide.createIcons()}function d(){let e=document.getElementById(`garden-grid`),n=document.getElementById(`garden-empty-state`);if(a(),t.length===0){e.style.display=`none`,n.style.display=`flex`;return}e.style.display=`grid`,n.style.display=`none`,e.innerHTML=t.map((e,t)=>{let n=new Date(e.lastWatered),r=Math.floor((Date.now()-n.getTime())/864e5),i=e.waterFrequencyDays-r,a=Math.max(0,Math.min(100,r/e.waterFrequencyDays*100)),o=`Water in ${i} day(s)`;return i<=0&&(o=`🚨 Needs Water Today!`),`
      <div class="garden-card">
        <img src="${e.image||`/images/monstera.png`}" alt="${e.name}" class="garden-thumb" />
        <div class="garden-info">
          <h4 class="garden-name">${e.name}</h4>
          <div class="garden-schedule">${o}</div>
          <div class="progress-bar-container">
            <div class="progress-fill" style="width: ${a}%;"></div>
          </div>
          <button class="water-action-btn" data-index="${t}">
            <i data-lucide="droplet"></i> Water Now
          </button>
        </div>
      </div>
    `}).join(``),e.querySelectorAll(`.water-action-btn`).forEach(e=>{e.addEventListener(`click`,t=>{t.stopPropagation(),f(parseInt(e.getAttribute(`data-index`),10))})});let r=document.getElementById(`btn-water-all`);r&&(r.onclick=()=>{t.forEach(e=>{e.lastWatered=new Date().toISOString()}),i(),d(),o(`💦 All plants in your garden have been watered!`)}),window.lucide&&window.lucide.createIcons()}function f(e){t[e]&&(t[e].lastWatered=new Date().toISOString(),i(),d(),o(`💦 ${t[e].name} has been refreshed!`))}function p(n){let r=e.find(e=>e.id===n);if(!r)return;let a=document.getElementById(`plant-modal`),s=document.getElementById(`modal-content`);s.innerHTML=`
    <div class="modal-plant-hero">
      <img src="${r.image}" alt="${r.name}" />
      <div class="modal-plant-hero-overlay">
        <h2>${r.name}</h2>
        <span style="color: var(--text-muted); font-style: italic;">${r.scientificName}</span>
      </div>
    </div>
    <div class="modal-plant-body">
      <p style="color: var(--text-muted); line-height: 1.6; margin-bottom: 1rem;">${r.description}</p>
      
      <div class="modal-grid-stats">
        <div class="modal-stat-box">
          <i data-lucide="sun" style="color: var(--sun-gold)"></i>
          <div style="font-size: 0.8rem; margin-top: 0.3rem;">${r.light}</div>
        </div>
        <div class="modal-stat-box">
          <i data-lucide="droplet" style="color: var(--water-blue)"></i>
          <div style="font-size: 0.8rem; margin-top: 0.3rem;">Every ${r.waterFrequencyDays} days</div>
        </div>
        <div class="modal-stat-box">
          <i data-lucide="thermometer" style="color: var(--accent-light)"></i>
          <div style="font-size: 0.8rem; margin-top: 0.3rem;">${r.temperature}</div>
        </div>
      </div>

      <h4 style="margin: 1.25rem 0 0.5rem 0; color: var(--accent-light);"><i data-lucide="sparkles"></i> Pro Care Tips</h4>
      <ul style="padding-left: 1.25rem; color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">
        ${r.careTips.map(e=>`<li style="margin-bottom: 0.4rem;">${e}</li>`).join(``)}
      </ul>

      <div style="margin-top: 1.5rem; text-align: right;">
        <button class="btn btn-primary" id="btn-modal-add-garden">
          <i data-lucide="plus"></i> Add to My Garden
        </button>
      </div>
    </div>
  `,a.classList.add(`active`),window.lucide&&window.lucide.createIcons(),document.getElementById(`btn-modal-add-garden`).onclick=()=>{t.some(e=>e.name===r.name)?o(`${r.name} is already in your garden!`,`info`):(t.push({id:r.id,name:r.name,image:r.image,waterFrequencyDays:r.waterFrequencyDays,lastWatered:new Date().toISOString()}),i(),d(),o(`🌱 Added ${r.name} to My Garden!`)),a.classList.remove(`active`)}}function m(){let e=document.getElementById(`btn-diagnose`),t=document.getElementById(`doctor-result`);e.addEventListener(`click`,()=>{let e=Array.from(document.querySelectorAll(`#symptoms-list input:checked`)).map(e=>e.value);if(e.length===0){o(`Please select at least one symptom to diagnose!`,`info`);return}let n=`Overwatering / Soil Drainage Issue`,r=`Moderate Severity`,i=[`Allow the top 2-3 inches of soil to dry out completely before watering again.`,`Ensure the plant pot has drainage holes at the bottom.`,`Check root system for brown, soft roots; prune rot with sterile scissors.`];e.includes(`brown_tips`)?(n=`Low Relative Humidity / Dry Air Burn`,r=`Mild Issue`,i=[`Increase humidity using a pebble tray with water under the pot.`,`Group humidity-loving plants together to create a microclimate.`,`Avoid keeping plant directly next to HVAC air conditioning vents.`]):e.includes(`white_webs`)?(n=`Spider Mite or Mealybug Infestation`,r=`High Priority`,i=[`Isolate plant immediately from other indoor plants.`,`Wipe leaves down thoroughly with organic Neem Oil spray or insecticidal soap.`,`Repeat leaf treatment every 5 days for 3 consecutive weeks.`]):e.includes(`root_rot`)&&(n=`Severe Root Rot (Pythium / Phytophthora)`,r=`Critical Risk`,i=[`Remove plant from pot and gently wash excess wet soil off roots.`,`Trim all black mushy roots back to healthy firm white tissue.`,`Repot in fresh sterile well-draining soil mix with extra perlite.`]),t.innerHTML=`
      <div class="diagnosis-result-content">
        <span class="diagnosis-tag">${r}</span>
        <h3>${n}</h3>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.95rem;">
          Based on selected symptoms, here is your step-by-step treatment protocol:
        </p>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${i.map((e,t)=>`
            <div class="remedy-step">
              <span class="step-num">${t+1}</span>
              <span style="font-size: 0.9rem; line-height: 1.5;">${e}</span>
            </div>
          `).join(``)}
        </div>

        <button class="btn btn-secondary btn-block" style="margin-top: 1.5rem;" id="btn-reset-doctor">
          <i data-lucide="refresh-cw"></i> Diagnose Another Plant
        </button>
      </div>
    `,window.lucide&&window.lucide.createIcons(),document.getElementById(`btn-reset-doctor`).onclick=()=>{document.querySelectorAll(`#symptoms-list input`).forEach(e=>e.checked=!1),t.innerHTML=`
        <div class="initial-doctor-state">
          <i data-lucide="heart-pulse" class="doctor-placeholder-icon"></i>
          <h3>Ready to Diagnose</h3>
          <p>Select one or more symptoms on the left and hit <strong>Run AI Diagnosis</strong> for personalized care instructions.</p>
        </div>
      `,window.lucide&&window.lucide.createIcons()}})}function h(){let e=document.getElementById(`calc-pot-type`),t=document.getElementById(`calc-light`),n=document.getElementById(`calc-temp`),r=document.getElementById(`calc-humidity`),i=document.getElementById(`val-temp`),a=document.getElementById(`val-humidity`),o=document.getElementById(`res-water-freq`),s=document.getElementById(`res-sun-advice`),c=document.getElementById(`res-humidity-advice`),l=()=>{let l=parseInt(n.value,10),u=parseInt(r.value,10),d=e.value,f=t.value;i.textContent=`${l}°C`,a.textContent=`${u}%`;let p=7;l>26?p-=2:l<18&&(p+=3),u<40?--p:u>65&&(p+=2),d===`terracotta`&&(p-=2),d===`fabric`&&(p-=3),f===`bright-direct`&&(p-=2),f===`low-light`&&(p+=4),o.textContent=`Every ${Math.max(2,p)} Days`,f===`bright-direct`?s.textContent=`High light intensity accelerates transpiration. Watch for sun scorched foliage.`:f===`low-light`?s.textContent=`Low light slows growth and water uptake. Water infrequently to prevent root sogginess.`:s.textContent=`Ideal bright indirect window exposure. Rotate pot 90° weekly for symmetrical growth.`,u<40?c.textContent=`Air is dry! Use a humidifier or mist regularly to prevent crispy brown tips.`:c.textContent=`Optimal tropical humidity level. Keeps leaves lush and vibrant.`};[e,t,n,r].forEach(e=>{e.addEventListener(`input`,l)})}function g(){let n=document.getElementById(`plant-modal`),r=document.getElementById(`add-plant-modal`);document.getElementById(`modal-close`).onclick=()=>n.classList.remove(`active`),document.getElementById(`add-modal-close`).onclick=()=>r.classList.remove(`active`),document.getElementById(`add-modal-cancel`).onclick=()=>r.classList.remove(`active`),document.getElementById(`btn-add-plant`).onclick=()=>{r.classList.add(`active`)};let a=document.getElementById(`form-add-plant`);a.addEventListener(`submit`,n=>{n.preventDefault();let s=document.getElementById(`add-name`).value,c=document.getElementById(`add-scientific`).value||`Houseplant`,l=document.getElementById(`add-category`).value,f=parseInt(document.getElementById(`add-water-days`).value,10)||7,p=document.getElementById(`add-light`).value,m={id:`custom-${Date.now()}`,name:s,scientificName:c,category:l,image:`/images/monstera.png`,waterFrequencyDays:f,light:p,humidity:`50-60%`,temperature:`20-25°C`,toxicity:`Unknown`,isPetSafe:!0,isLowLight:p===`Low Light`,isAirPurifying:!0,difficulty:`Easy`,description:`Custom user-added houseplant.`,careTips:[`Water regularly based on soil dampness.`,`Provide recommended sunlight.`]};e.unshift(m),u(),t.push({id:m.id,name:m.name,image:m.image,waterFrequencyDays:f,lastWatered:new Date().toISOString()}),i(),d(),r.classList.remove(`active`),a.reset(),o(`🎉 Added ${s} to your Plant Collection!`)})}}))();