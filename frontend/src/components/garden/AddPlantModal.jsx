import React, { useState } from 'react';
import { X } from 'lucide-react';

export default function AddPlantModal({ isOpen, onClose, onAddPlant }) {
  const [name, setName] = useState('');
  const [species, setSpecies] = useState('');

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name.trim()) return;
    onAddPlant({
      name: name.trim(),
      species: species.trim() || 'Indoor Plant'
    });
    setName('');
    setSpecies('');
    onClose();
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem' }}>🌱 Add Plant Profile</h3>
          <button className="btn-icon" onClick={onClose}><X size={18} /></button>
        </div>
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <input 
            type="text" 
            className="auth-input" 
            placeholder="Plant Name" 
            value={name} 
            onChange={e => setName(e.target.value)} 
            required 
          />
          <input 
            type="text" 
            className="auth-input" 
            placeholder="Species (e.g. Monstera, Tomato)" 
            value={species} 
            onChange={e => setSpecies(e.target.value)} 
          />
          <button type="submit" className="btn-primary">Add to My Garden</button>
        </form>
      </div>
    </div>
  );
}
