// API Service for PlantCare AI Frontend

const API_BASE = '';

/**
 * Authenticate user with username/email and password
 */
export async function loginUser(identifier, password) {
  const response = await fetch(`${API_BASE}/api/v1/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ identifier, password })
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || 'Login failed. Please check your credentials.');
  }
  return data;
}

/**
 * Register a new user account
 */
export async function registerUser(userData) {
  const response = await fetch(`${API_BASE}/api/v1/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData)
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || 'Registration failed.');
  }
  return data;
}

/**
 * Request password reset
 */
export async function resetPassword(email) {
  const response = await fetch(`${API_BASE}/api/v1/auth/forgot-password`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || 'Password reset request failed.');
  }
  return data;
}

/**
 * Upload leaf image for AI diagnosis
 */
export async function uploadDiagnosis(file) {
  const formData = new FormData();
  formData.append('image', file);
  formData.append('file', file);

  const response = await fetch(`${API_BASE}/api/v1/diagnose`, {
    method: 'POST',
    body: formData
  });

  if (!response.ok) {
    throw new Error(`Diagnosis server error: ${response.status}`);
  }
  return await response.json();
}

/**
 * Fetch past diagnosis history
 */
export async function fetchHistory() {
  const response = await fetch(`${API_BASE}/api/v1/history`);
  if (!response.ok) {
    throw new Error('Failed to fetch history');
  }
  return await response.json();
}

/**
 * Clear diagnosis history
 */
export async function clearHistory() {
  const response = await fetch(`${API_BASE}/api/v1/history`, {
    method: 'DELETE'
  });
  return response.ok;
}
