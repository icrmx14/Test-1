import { useState } from 'react';
import api from '../services/api';

const tabs = [
  'AI Chatbot',
  'Workload Heatmaps',
  'Burnout Detection',
  'Idle Resources',
  'Cost Reduction',
  'Inventory Optimization',
  'Reorder Recommendations',
];

export default function AIAssistant() {
  const [activeTab, setActiveTab] = useState(tabs[0]);
  const [messages, setMessages] = useState([
    { role: 'assistant', text: 'Hello! I am your ERP Copilot. Ask me anything about demand forecasts, employee workload, or low stock reorder points!' }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [sending, setSending] = useState(false);

  const sendMessage = async () => {
    if (!inputValue.trim()) return;
    const userMsg = inputValue;
    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setInputValue('');
    setSending(true);

    try {
      const res = await api.post(`/api/v1/ai/copilot/chat?message=${encodeURIComponent(userMsg)}`);
      setMessages(prev => [...prev, { role: 'assistant', text: res.data.reply }]);
    } catch (err) {
      console.error(err);
      setMessages(prev => [...prev, { role: 'assistant', text: 'Error connecting to the AI service. Please make sure the backend is running.' }]);
    } finally {
      setSending(false);
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">AI Terminal & Executive Assistant</h2>
      <div className="flex flex-wrap gap-2 mb-6">
        {tabs.map(tab => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className="px-3 py-1 rounded-full text-sm transition-colors"
            style={{
              background: activeTab === tab ? 'var(--color-primary)' : 'var(--color-card)',
              color: activeTab === tab ? '#fff' : 'var(--color-fg)',
              border: '1px solid var(--color-border)',
            }}
          >
            {tab}
          </button>
        ))}
      </div>
      {activeTab === 'AI Chatbot' ? (
        <div
          className="rounded-xl p-6 min-h-[400px] flex flex-col"
          style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}
        >
          <div className="flex-1 overflow-y-auto mb-4 space-y-2 max-h-[300px]">
            {messages.map((m, idx) => (
              <div
                key={idx}
                className={`p-3 rounded-lg max-w-[75%] ${
                  m.role === 'user'
                    ? 'ml-auto bg-blue-600 text-white'
                    : 'bg-gray-100 text-gray-900 border border-gray-200'
                }`}
              >
                {m.text}
              </div>
            ))}
            {sending && <div className="text-xs opacity-50">Copilot is thinking...</div>}
          </div>
          <div className="flex gap-2">
            <input
              type="text"
              value={inputValue}
              onChange={e => setInputValue(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && sendMessage()}
              placeholder='Ask anything… e.g. "Who is available tomorrow?"'
              className="flex-1 px-4 py-2 rounded-lg"
              style={{ background: 'var(--color-bg)', border: '1px solid var(--color-border)', color: 'var(--color-fg)' }}
            />
            <button
              onClick={sendMessage}
              disabled={sending}
              className="px-4 py-2 rounded-lg font-medium transition-opacity hover:opacity-90"
              style={{ background: 'var(--color-primary)', color: '#fff' }}
            >
              Send
            </button>
          </div>
        </div>
      ) : (
        <div
          className="rounded-xl p-6 min-h-[300px]"
          style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}
        >
          <p className="opacity-60">Panel: {activeTab}</p>
          <div className="mt-2 text-sm">
            {activeTab === 'Workload Heatmaps' && <p>All active employee capacity allocations are under normal thresholds.</p>}
            {activeTab === 'Burnout Detection' && <p>No employees are currently identified with high burnout risk (&gt;90% utilization).</p>}
            {activeTab === 'Idle Resources' && <p>No idle resources detected. All bookable assets are properly scheduled.</p>}
            {activeTab === 'Cost Reduction' && <p>AI Suggestion: Re-route Supplier shipments via Hub B to save 12% logistics cost.</p>}
            {activeTab === 'Inventory Optimization' && <p>AI Suggestion: Safety Stock for SKU-001 should be increased to 15 units based on seasonal demand.</p>}
            {activeTab === 'Reorder Recommendations' && <p>AI Suggestion: Trigger Reorder for Raw Material A immediately.</p>}
          </div>
        </div>
      )}
    </div>
  );
}
