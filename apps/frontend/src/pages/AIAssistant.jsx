import { useState } from 'react';

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
          <div className="flex-1 overflow-y-auto mb-4">
            <p className="opacity-60">Chat messages will appear here...</p>
          </div>
          <div className="flex gap-2">
            <input
              type="text"
              placeholder='Ask anything… e.g. "Who is available tomorrow?"'
              className="flex-1 px-4 py-2 rounded-lg"
              style={{ background: 'var(--color-bg)', border: '1px solid var(--color-border)', color: 'var(--color-fg)' }}
            />
            <button
              className="px-4 py-2 rounded-lg font-medium"
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
          <div>Stub</div>
        </div>
      )}
    </div>
  );
}
