// Initial Garden Plants and Reminders Database
export const INITIAL_PLANT_PROFILES = [
  { id: 1, name: 'Monstera Deliciosa', species: 'Monstera', room: 'Living Room', healthScore: 92, lastWatered: '2 days ago', status: 'Healthy' },
  { id: 2, name: 'Ficus Lyrata (Fiddle Leaf)', species: 'Fiddle Leaf Fig', room: 'Balcony', healthScore: 45, lastWatered: '5 days ago', status: 'Mild Chlorosis' },
  { id: 3, name: 'Cherry Tomato Pot', species: 'Tomato', room: 'Garden', healthScore: 78, lastWatered: '1 day ago', status: 'Healthy' }
];

export const INITIAL_REMINDERS = [
  { id: 1, plant: 'Ficus Lyrata', task: 'Watering & Neem Spray', dueDate: 'Today', urgent: true },
  { id: 2, plant: 'Monstera Deliciosa', task: 'Soil Moisture Check', dueDate: 'Tomorrow', urgent: false },
  { id: 3, plant: 'Cherry Tomato', task: 'NPK Liquid Fertilizer', dueDate: 'In 3 days', urgent: false }
];

export const WEATHER_FORECAST = {
  city: 'Local Region',
  temp: '28°C',
  humidity: '82%',
  riskLevel: 'HIGH FUNGAL RISK',
  advice: 'High humidity increases Late Blight & Powdery Mildew risk. Avoid overhead watering.'
};
