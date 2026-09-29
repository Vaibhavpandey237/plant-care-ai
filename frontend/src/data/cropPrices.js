// Crop Price & Government MSP Database (Rates in ₹ per Quintal)
export const CROP_PRICES_DATABASE = [
  {
    id: 'wheat',
    name: 'Wheat (Gehu)',
    category: 'Cereal',
    mspINR: 2275,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Punjab',
        mandis: [
          { mandiName: 'Khanna Mandi', minPrice: 2280, maxPrice: 2420, modalPrice: 2350, arrivalQuintals: 4500, date: '20-Aug-2026' },
          { mandiName: 'Rajpura Mandi', minPrice: 2275, maxPrice: 2390, modalPrice: 2320, arrivalQuintals: 3200, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Haryana',
        mandis: [
          { mandiName: 'Karnal Mandi', minPrice: 2290, maxPrice: 2450, modalPrice: 2380, arrivalQuintals: 5100, date: '20-Aug-2026' },
          { mandiName: 'Kurukshetra Mandi', minPrice: 2280, maxPrice: 2400, modalPrice: 2340, arrivalQuintals: 3800, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Uttar Pradesh',
        mandis: [
          { mandiName: 'Bareilly Mandi', minPrice: 2275, maxPrice: 2380, modalPrice: 2310, arrivalQuintals: 6200, date: '20-Aug-2026' },
          { mandiName: 'Agra Mandi', minPrice: 2280, maxPrice: 2410, modalPrice: 2350, arrivalQuintals: 4900, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Madhya Pradesh',
        mandis: [
          { mandiName: 'Indore Mandi', minPrice: 2300, maxPrice: 2520, modalPrice: 2420, arrivalQuintals: 7500, date: '20-Aug-2026' },
          { mandiName: 'Ujjain Mandi', minPrice: 2290, maxPrice: 2480, modalPrice: 2390, arrivalQuintals: 5400, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'paddy',
    name: 'Paddy / Rice (Dhan)',
    category: 'Cereal',
    mspINR: 2183,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Haryana',
        mandis: [
          { mandiName: 'Ambala Mandi', minPrice: 2200, maxPrice: 2380, modalPrice: 2290, arrivalQuintals: 3900, date: '20-Aug-2026' },
          { mandiName: 'Kaithal Mandi', minPrice: 2210, maxPrice: 2410, modalPrice: 2320, arrivalQuintals: 4200, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Punjab',
        mandis: [
          { mandiName: 'Amritsar Mandi', minPrice: 2205, maxPrice: 2390, modalPrice: 2300, arrivalQuintals: 4800, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Uttar Pradesh',
        mandis: [
          { mandiName: 'Gorakhpur Mandi', minPrice: 2190, maxPrice: 2350, modalPrice: 2270, arrivalQuintals: 5300, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'mustard',
    name: 'Mustard / Rapeseed (Sarson)',
    category: 'Oilseed',
    mspINR: 5650,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Rajasthan',
        mandis: [
          { mandiName: 'Bharatpur Mandi', minPrice: 5700, maxPrice: 6150, modalPrice: 5920, arrivalQuintals: 2800, date: '20-Aug-2026' },
          { mandiName: 'Alwar Mandi', minPrice: 5680, maxPrice: 6100, modalPrice: 5880, arrivalQuintals: 3100, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Haryana',
        mandis: [
          { mandiName: 'Hisar Mandi', minPrice: 5670, maxPrice: 6050, modalPrice: 5850, arrivalQuintals: 2200, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'cotton',
    name: 'Cotton (Kapas)',
    category: 'Commercial',
    mspINR: 6620,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Gujarat',
        mandis: [
          { mandiName: 'Rajkot Mandi', minPrice: 6750, maxPrice: 7250, modalPrice: 7000, arrivalQuintals: 3400, date: '20-Aug-2026' },
          { mandiName: 'Kadi Mandi', minPrice: 6700, maxPrice: 7180, modalPrice: 6940, arrivalQuintals: 2900, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Maharashtra',
        mandis: [
          { mandiName: 'Yavatmal Mandi', minPrice: 6680, maxPrice: 7100, modalPrice: 6890, arrivalQuintals: 4100, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'maize',
    name: 'Maize (Makka)',
    category: 'Cereal',
    mspINR: 2090,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Madhya Pradesh',
        mandis: [
          { mandiName: 'Chhindwara Mandi', minPrice: 2100, maxPrice: 2280, modalPrice: 2180, arrivalQuintals: 3600, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Karnataka',
        mandis: [
          { mandiName: 'Davanagere Mandi', minPrice: 2110, maxPrice: 2300, modalPrice: 2205, arrivalQuintals: 2900, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'gram',
    name: 'Gram (Chana)',
    category: 'Pulses',
    mspINR: 5440,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Maharashtra',
        mandis: [
          { mandiName: 'Latur Mandi', minPrice: 5500, maxPrice: 5850, modalPrice: 5680, arrivalQuintals: 2100, date: '20-Aug-2026' }
        ]
      },
      {
        stateName: 'Rajasthan',
        mandis: [
          { mandiName: 'Bikaner Mandi', minPrice: 5480, maxPrice: 5800, modalPrice: 5640, arrivalQuintals: 1900, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'bajra',
    name: 'Bajra (Pearl Millet)',
    category: 'Millet',
    mspINR: 2500,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Rajasthan',
        mandis: [
          { mandiName: 'Jaipur Mandi', minPrice: 2520, maxPrice: 2700, modalPrice: 2610, arrivalQuintals: 2400, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'jowar',
    name: 'Jowar (Sorghum)',
    category: 'Millet',
    mspINR: 3180,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Maharashtra',
        mandis: [
          { mandiName: 'Solapur Mandi', minPrice: 3200, maxPrice: 3450, modalPrice: 3320, arrivalQuintals: 1800, date: '20-Aug-2026' }
        ]
      }
    ]
  },
  {
    id: 'pulses',
    name: 'Pulses (Tur / Moong)',
    category: 'Pulses',
    mspINR: 7000,
    mspYear: '2025-26',
    states: [
      {
        stateName: 'Madhya Pradesh',
        mandis: [
          { mandiName: 'Hardoi Mandi', minPrice: 7200, maxPrice: 8800, modalPrice: 8100, arrivalQuintals: 1500, date: '20-Aug-2026' }
        ]
      }
    ]
  }
];
