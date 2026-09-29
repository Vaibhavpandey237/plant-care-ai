// Recommended Products & Remedies Database
export const RECOMMENDED_PRODUCTS_DATABASE = [
  {
    id: 'blitox-copper-fungicide',
    name: 'Blitox 50% WP Copper Oxychloride',
    brand: 'Tata Rallis Ltd.',
    category: 'Fungicide',
    categoryClass: 'cat-fungicide',
    suitableCropDisease: 'Potato Early & Late Blight, Tomato Leaf Spot, Grape Black Rot',
    packSize: '500 grams',
    dosage: '2.5 g per liter of water. Spray evenly over foliage early morning or late evening.',
    safetyPrecautions: '⚠️ Wear protective gloves, safety goggles & mask. Keep out of reach of children.',
    priceINR: 340,
    lastUpdatedDate: '20-Aug-2026',
    buyNowLink: 'https://www.bighaat.com',
    image: '🧪',
    diseaseKey: 'blight',
    alternatives: [
      { name: 'Tata Master 72% WP', brand: 'Tata Rallis', priceINR: 310, note: 'Save ₹30 (Standard Fungicide)' },
      { name: 'Antracol 70% WP', brand: 'Bayer CropScience', priceINR: 365, note: 'Premium Zinc-based protectant' }
    ]
  },
  {
    id: 'neem-oil-organic',
    name: 'Cold Pressed Organic Neem Oil (1500 PPM)',
    brand: 'Indore Bio Organics',
    category: 'Bio-pesticide',
    categoryClass: 'cat-bio',
    suitableCropDisease: 'Rice Stem Borer, Aphids, Whiteflies, Thrips, Spider Mites',
    packSize: '1 Liter',
    dosage: '5 ml per liter of water + 2-3 drops liquid dish soap as emulsifier. Spray weekly.',
    safetyPrecautions: '🌿 100% Eco-friendly & non-toxic to honeybees when sprayed after sunset.',
    priceINR: 420,
    lastUpdatedDate: '19-Aug-2026',
    buyNowLink: 'https://www.agribegri.com',
    image: '🌿',
    diseaseKey: 'pesticide',
    alternatives: [
      { name: 'Katyayani Neem 3000 PPM', brand: 'Katyayani Organics', priceINR: 480, note: 'Higher Azadirachtin conc.' },
      { name: 'Organic India Neem Care', brand: 'Organic India', priceINR: 390, note: 'Save ₹30 (Standard grade)' }
    ]
  },
  {
    id: 'epsom-salt-magnesium',
    name: 'Epsom Salt Magnesium Sulfate (9.5% Mg)',
    brand: 'IFFCO Urban Gardens',
    category: 'Fertilizer',
    categoryClass: 'cat-fertilizer',
    suitableCropDisease: 'Chlorosis (Yellowing Leaves), Tomato Blossom Rot, Pepper, Roses',
    packSize: '1 kg',
    dosage: 'Foliar Spray: 10g per gallon of water. Soil Drench: 15g per plant base monthly.',
    safetyPrecautions: '✅ Safe & non-hazardous. Store sealed in a dry place away from direct moisture.',
    priceINR: 180,
    lastUpdatedDate: '20-Aug-2026',
    buyNowLink: 'https://www.iffcostore.in',
    image: '💎',
    diseaseKey: 'yellow',
    alternatives: [
      { name: 'Katyayani Epsom Salt', brand: 'Katyayani', priceINR: 160, note: 'Save ₹20 (Bulk Pack)' },
      { name: 'Syngenta MagBoost', brand: 'Syngenta', priceINR: 210, note: 'Added Micronutrients' }
    ]
  },
  {
    id: 'ferterra-chlorantraniliprole',
    name: 'Ferterra 0.4% GR Insecticide',
    brand: 'FMC India Ltd.',
    category: 'Pesticide',
    categoryClass: 'cat-pesticide',
    suitableCropDisease: 'Rice Stem Borer, Sugarcane Top Borer, Corn Armyworm',
    packSize: '4 kg',
    dosage: '4 kg per acre applied via soil broadcasting during early crop stage.',
    safetyPrecautions: '⚠️ Do not apply directly to open water streams. Wash hands thoroughly after handling.',
    priceINR: 685,
    lastUpdatedDate: '18-Aug-2026',
    buyNowLink: 'https://www.krishibazaar.in',
    image: '🌾',
    diseaseKey: 'rice',
    alternatives: [
      { name: 'Dhanuka Cover 0.4% GR', brand: 'Dhanuka Agritech', priceINR: 650, note: 'Save ₹35 (Generic Alt)' },
      { name: 'Syngenta Virtako 0.6% GR', brand: 'Syngenta', priceINR: 720, note: 'Dual-action Insecticide' }
    ]
  },
  {
    id: 'npk-19-19-19-water-soluble',
    name: 'Mahadhan 19:19:19 Water Soluble NPK',
    brand: 'Smartchem Technologies (Mahadhan)',
    category: 'Fertilizer',
    categoryClass: 'cat-fertilizer',
    suitableCropDisease: 'All Vegetables & Crops, Nitrogen/Phosphorus/Potassium Stunting',
    packSize: '1 kg',
    dosage: '5 g per liter of water applied every 14 days during active growth phase.',
    safetyPrecautions: '✅ Keep container tightly closed in a cool, ventilated shade.',
    priceINR: 210,
    lastUpdatedDate: '20-Aug-2026',
    buyNowLink: 'https://www.mahadhan.co.in',
    image: '⚡',
    diseaseKey: 'general',
    alternatives: [
      { name: 'IFFCO NPK 19-19-19', brand: 'IFFCO', priceINR: 195, note: 'Save ₹15 (Farmer Choice)' },
      { name: 'Nagarjuna SoluFert NPK', brand: 'Nagarjuna', priceINR: 225, note: 'Imported Quality' }
    ]
  }
];
