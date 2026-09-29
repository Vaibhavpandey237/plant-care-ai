import React, { useState } from 'react';
import { 
  Upload, CheckCircle2, RefreshCw, Activity, ShieldAlert, 
  ShoppingCart, ExternalLink, AlertCircle 
} from 'lucide-react';
import { RECOMMENDED_PRODUCTS_DATABASE } from '../../data/products';

export default function DiagnosisView({ onDiagnosisComplete }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [imageError, setImageError] = useState('');
  const [dragActive, setDragActive] = useState(false);

  const checkIsPlantImage = (imageFile) => {
    return new Promise((resolve) => {
      const img = new Image();
      img.src = URL.createObjectURL(imageFile);
      img.onload = () => {
        try {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          canvas.width = 120;
          canvas.height = 120;
          ctx.drawImage(img, 0, 0, 120, 120);
          const imgData = ctx.getImageData(0, 0, 120, 120).data;

          let plantPixels = 0;
          let faceSkinPixels = 0;
          const totalPixels = 120 * 120;

          for (let i = 0; i < imgData.length; i += 4) {
            const r = imgData[i];
            const g = imgData[i + 1];
            const b = imgData[i + 2];

            // Inclusive Plant Foliage Detection (Green, Chlorosis Yellow, Brown Necrosis, Stems)
            if ((g > r - 15 && g > b - 15) || (r > 60 && g > 50 && b < 140) || (r > 50 && g > 30)) {
              plantPixels++;
            }

            // Strict Human Face Close-Up Skin Check
            if (r > 140 && g > 90 && b > 70 && (r > g + 20) && (g > b + 10) && g < 170) {
              faceSkinPixels++;
            }
          }

          const plantRatio = plantPixels / totalPixels;
          const faceSkinRatio = faceSkinPixels / totalPixels;

          if (faceSkinRatio > 0.45 && plantRatio < 0.03) {
            resolve(false);
          } else if (plantRatio < 0.01 && faceSkinRatio > 0.20) {
            resolve(false);
          } else {
            resolve(true);
          }
        } catch (e) {
          resolve(true);
        }
      };
      img.onerror = () => resolve(true);
    });
  };

  const handleFileSelect = (file) => {
    setImageError('');
    setResult(null);
    if (file && file.type.startsWith('image/')) {
      setSelectedFile(file);
      setPreviewUrl(URL.createObjectURL(file));
    }
  };

  const handleAnalyze = async () => {
    if (!selectedFile) return;
    setLoading(true);
    setImageError('');
    setResult(null);

    const isValidPlant = await checkIsPlantImage(selectedFile);
    if (!isValidPlant) {
      setImageError("Invalid Image: Please upload a clear plant leaf or crop photo only. Non-plant images (such as human faces or objects) are not allowed.");
      setResult(null);
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedFile);
    formData.append('file', selectedFile);

    try {
      const response = await fetch('/api/v1/diagnose', {
        method: 'POST',
        body: formData,
      });

      if (response.status === 422) {
        const data = await response.json();
        setImageError(data.message || "Invalid Image: Please upload a clear plant leaf or crop photo only.");
        setResult(null);
        return;
      }

      if (response.ok) {
        const data = await response.json();
        if (data.error === 'NON_PLANT_IMAGE' || !data.topPrediction) {
          setImageError("Invalid Image: Please upload a clear plant leaf or crop photo only.");
          setResult(null);
        } else {
          setResult(data);
          if (onDiagnosisComplete) onDiagnosisComplete(data);
        }
      } else {
        setImageError("Invalid Image: Please upload a clear plant leaf or crop photo only.");
        setResult(null);
      }
    } catch (err) {
      setImageError("Invalid Image: Please upload a clear plant leaf or crop photo only.");
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="main-grid">
      {/* Uploader Section */}
      <section className="card">
        <h2 className="card-title">
          <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Upload size={20} color="var(--accent-green)" /> Leaf Photo Upload
          </span>
        </h2>
        <p className="card-subtitle">Upload leaf image for Java `BufferedImage` analysis & DJL AI tensor classification.</p>

        {imageError && (
          <div className="alert-box alert-error" style={{ marginBottom: '1rem' }}>
            <AlertCircle size={16} style={{ display: 'inline', marginRight: '6px' }} />
            {imageError}
          </div>
        )}

        <div
          className={`dropzone ${dragActive ? 'drag-active' : ''}`}
          onDragOver={(e) => { e.preventDefault(); setDragActive(true); }}
          onDragLeave={() => setDragActive(false)}
          onDrop={(e) => { e.preventDefault(); setDragActive(false); handleFileSelect(e.dataTransfer.files[0]); }}
          onClick={() => document.getElementById('file-input').click()}
        >
          <input type="file" id="file-input" accept="image/*" style={{ display: 'none' }} onChange={(e) => handleFileSelect(e.target.files[0])} />
          {previewUrl ? (
            <img src={previewUrl} alt="Leaf Preview" className="preview-img" />
          ) : (
            <>
              <Upload className="upload-icon" />
              <p style={{ fontWeight: 600 }}>Drag & Drop leaf photo here</p>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Supports PNG, JPG, WEBP up to 10MB</p>
            </>
          )}
        </div>

        <button className="btn-primary" onClick={handleAnalyze} disabled={!selectedFile || loading}>
          {loading ? <><RefreshCw size={18} className="spin" /> Running DJL Inference...</> : <><Activity size={18} /> Analyze Plant Health</>}
        </button>
      </section>

      {/* Diagnostic Results Section */}
      <section className="card">
        <h2 className="card-title">
          <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <CheckCircle2 size={20} color="var(--accent-teal)" /> Diagnostic Results
          </span>
        </h2>

        {result ? (
          <div>
            <div className="gauge-box">
              <div className="score-circle" style={{ '--score': result.healthScore }}>
                <span className="score-text">{result.healthScore}</span>
              </div>
              <div>
                <h3 style={{ fontSize: '1.1rem' }}>{result.recommendations?.display_name || result.topPrediction}</h3>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginTop: '0.25rem' }}>
                  <span className={`severity-badge severity-${(result.severity || 'MODERATE').toLowerCase()}`}>
                    Severity: {result.severity || 'MODERATE'}
                  </span>
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                    🎯 Confidence: {(result.confidencePct || 0).toFixed(1)}%
                  </span>
                </div>
              </div>
            </div>

            <h4 style={{ fontSize: '0.95rem', margin: '1rem 0 0.5rem', color: 'var(--accent-teal)' }}>
              💊 Treatment & Action Steps
            </h4>
            {result.recommendations?.recommendations?.map((rec, idx) => (
              <div key={idx} className="rec-item">
                <span style={{ fontWeight: 700, fontSize: '0.85rem', color: 'var(--accent-teal)' }}>[{rec.category}]</span>
                <p style={{ fontSize: '0.88rem' }}>{rec.text}</p>
              </div>
            ))}

            {/* Recommended Pesticides & Remedies */}
            <div style={{ marginTop: '1.5rem', paddingTop: '1.25rem', borderTop: '1px solid var(--bg-card-border)' }}>
              <h4 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '0.75rem', color: 'var(--accent-green)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <ShoppingCart size={18} /> Recommended Pesticides & Remedies for {result.recommendations?.display_name || 'Detected Crop'}
              </h4>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                {RECOMMENDED_PRODUCTS_DATABASE
                  .filter(prod => {
                    const pred = (result.topPrediction || result.recommendations?.condition || '').toLowerCase();
                    if (pred.includes('blight')) return prod.diseaseKey === 'blight' || prod.diseaseKey === 'pesticide';
                    if (pred.includes('spot') || pred.includes('yellow')) return prod.diseaseKey === 'yellow' || prod.diseaseKey === 'blight';
                    if (pred.includes('rice')) return prod.diseaseKey === 'rice' || prod.diseaseKey === 'pesticide';
                    return true;
                  })
                  .slice(0, 3)
                  .map(prod => (
                    <div key={prod.id} className="product-card" style={{ padding: '1rem' }}>
                      <div className="product-header">
                        <span style={{ fontSize: '1.8rem', padding: '0.4rem', background: 'var(--input-bg)', borderRadius: '10px' }}>{prod.image}</span>
                        <div style={{ flex: 1 }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                            <h5 style={{ fontSize: '0.95rem', fontWeight: 700 }}>{prod.name}</h5>
                            <span className="price-inr" style={{ fontSize: '1.1rem' }}>₹{prod.priceINR}</span>
                          </div>
                          <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>Brand: {prod.brand}</p>
                          <span className={`cat-badge ${prod.categoryClass}`} style={{ marginTop: '0.2rem', display: 'inline-block' }}>{prod.category}</span>
                        </div>
                      </div>

                      <div style={{ fontSize: '0.8rem', display: 'flex', flexDirection: 'column', gap: '0.35rem', marginTop: '0.5rem' }}>
                        <p>🌱 <strong>Suitable Crop & Disease:</strong> {prod.suitableCropDisease}</p>
                        <p>📦 <strong>Pack Size:</strong> {prod.packSize}</p>
                        <p>💊 <strong>Dosage & Application Method:</strong> {prod.dosage}</p>
                        <p style={{ fontSize: '0.75rem', color: '#F59E0B', background: 'rgba(245,158,11,0.1)', padding: '0.35rem', borderRadius: '6px' }}>
                          {prod.safetyPrecautions}
                        </p>
                      </div>

                      <div style={{ marginTop: '0.75rem', paddingTop: '0.5rem', borderTop: '1px solid var(--bg-card-border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Updated: {prod.lastUpdatedDate}</span>
                        <a href={prod.buyNowLink} target="_blank" rel="noopener noreferrer" className="buy-btn" style={{ padding: '0.4rem 0.85rem', fontSize: '0.8rem' }}>
                          Buy Now <ExternalLink size={12} />
                        </a>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          </div>
        ) : (
          <div style={{ textAlign: 'center', padding: '3rem 1rem', color: 'var(--text-muted)' }}>
            <ShieldAlert size={44} style={{ margin: '0 auto 0.75rem', opacity: 0.5 }} />
            <p>Upload a leaf image to generate Health Score (0-100), Severity, Confidence %, and Care Instructions.</p>
          </div>
        )}
      </section>
    </main>
  );
}
