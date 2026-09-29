import React from 'react';
import { ShoppingCart, ExternalLink } from 'lucide-react';
import { RECOMMENDED_PRODUCTS_DATABASE } from '../../data/products';

export default function ProductsStoreView() {
  return (
    <section className="card">
      <div className="card-title" style={{ marginBottom: '0.5rem' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <ShoppingCart size={22} color="var(--accent-green)" /> Fertilizer & Pesticide Recommendations Module
        </span>
      </div>
      <p className="card-subtitle">
        Verified treatment products categorized by crop, disease, pack size, dose, INR price, and price comparison.
      </p>

      <div className="product-grid">
        {RECOMMENDED_PRODUCTS_DATABASE.map(prod => (
          <div key={prod.id} className="product-card">
            <div>
              <div className="product-header">
                <span style={{ fontSize: '2.2rem', padding: '0.6rem', background: 'var(--input-bg)', borderRadius: '12px' }}>
                  {prod.image}
                </span>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <h4 style={{ fontSize: '1rem', fontWeight: 700 }}>{prod.name}</h4>
                  </div>
                  <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Brand: {prod.brand}</p>
                  <span className={`cat-badge ${prod.categoryClass}`} style={{ marginTop: '0.3rem', display: 'inline-block' }}>
                    {prod.category}
                  </span>
                </div>
              </div>

              <div style={{ fontSize: '0.84rem', display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
                <p>🌱 <strong>Suitable Crop & Disease:</strong> {prod.suitableCropDisease}</p>
                <p>📦 <strong>Pack Size:</strong> {prod.packSize}</p>
                <p>💊 <strong>Dosage & Method:</strong> {prod.dosage}</p>
                <p style={{ fontSize: '0.8rem', color: '#F59E0B', background: 'rgba(245,158,11,0.1)', padding: '0.4rem', borderRadius: '6px' }}>
                  {prod.safetyPrecautions}
                </p>
              </div>
            </div>

            <div style={{ marginTop: '1rem', paddingTop: '0.75rem', borderTop: '1px solid var(--bg-card-border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <span className="price-inr">₹{prod.priceINR}</span>
                <p style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Last updated: {prod.lastUpdatedDate}</p>
              </div>
              <a href={prod.buyNowLink} target="_blank" rel="noopener noreferrer" className="buy-btn">
                Buy Now <ExternalLink size={14} />
              </a>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
