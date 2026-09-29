import React, { useState } from 'react';
import { MessageSquare, Send } from 'lucide-react';

export default function BotanistChatView() {
  const [chatMessages, setChatMessages] = useState([
    { sender: 'bot', text: '🌱 Hello! I am your AI Botanist. Ask me about pesticides, fungicides, fertilizers, or leaf disease treatments.' }
  ]);
  const [chatInput, setChatInput] = useState('');

  const generateBotanistResponse = (userText) => {
    const lower = userText.toLowerCase().trim();
    if (lower.includes('price') || lower.includes('msp') || lower.includes('mandi') || lower.includes('rate')) {
      return "🌾 Check out our 'Crop Prices' tab on the navigation bar to see Govt MSP rates in ₹/quintal and live Mandi market rates!";
    }
    if (lower.includes('rice')) {
      return "🌾 For Rice: Recommended pesticides for Stem Borer include Chlorantraniliprole (Ferterra) or Cartap Hydrochloride. Current Govt MSP is ₹2,183/quintal.";
    }
    if (lower.includes('wheat')) {
      return "🌾 For Wheat: For Rust & Powdery Mildew, spray Propiconazole 25% EC (Tilt). Current Govt MSP is ₹2,275/quintal.";
    }
    return "🌿 AI Botanist: Maintain proper soil drainage, avoid overhead leaf watering, and inspect foliage weekly for early signs of pests.";
  };

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!chatInput.trim()) return;

    const userText = chatInput;
    setChatMessages(prev => [...prev, { sender: 'user', text: userText }]);
    setChatInput('');

    setTimeout(() => {
      const botReply = generateBotanistResponse(userText);
      setChatMessages(prev => [...prev, { sender: 'bot', text: botReply }]);
    }, 600);
  };

  return (
    <section className="card">
      <h2 className="card-title" style={{ marginBottom: '1rem' }}>
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <MessageSquare size={22} color="var(--accent-green)" /> AI Botanist Assistant
        </span>
      </h2>
      <div className="chat-box">
        <div className="chat-messages">
          {chatMessages.map((msg, idx) => (
            <div key={idx} className={`chat-bubble ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <form onSubmit={handleSendMessage} className="chat-input-row">
          <input
            type="text"
            className="chat-input"
            placeholder="Ask about plant diseases, pesticides, crop prices..."
            value={chatInput}
            onChange={(e) => setChatInput(e.target.value)}
          />
          <button type="submit" className="btn-secondary">
            <Send size={16} />
          </button>
        </form>
      </div>
    </section>
  );
}
