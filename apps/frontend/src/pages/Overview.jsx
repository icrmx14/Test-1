import { useState } from 'react';

const tabs = [
  'Executive KPIs',
  'Employee Availability',
  'Attendance Summary',
  'Project Status',
  'Pending Approvals',
  'Inventory Alerts',
  'Revenue Trend',
  'AI Insights',
];

export default function Overview() {
  const [activeTab, setActiveTab] = useState(tabs[0]);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Overview Dashboard</h2>
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
      <div
        className="rounded-xl p-6 min-h-[300px]"
        style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}
      >
        <p className="opacity-60">Widget: {activeTab}</p>
        <div>Stub</div>
      </div>
    </div>
  );
}
