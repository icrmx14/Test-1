import { useState } from 'react';
import api from '../services/api';

const panels = [
  'Company Profile',
  'Branch / Cost Centers',
  'User Management',
  'RBAC / SSO',
  'System Health',
  'Database Backup',
];

export default function Settings() {
  const [activePanel, setActivePanel] = useState(panels[0]);
  const [healthStatus, setHealthStatus] = useState(null);

  const checkHealth = async () => {
    try {
      const res = await api.get('/api/v1/health');
      setHealthStatus(res.data);
    } catch {
      setHealthStatus({ status: 'error' });
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">System Settings & Admin</h2>
      <div className="flex flex-wrap gap-2 mb-6">
        {panels.map(p => (
          <button
            key={p}
            onClick={() => setActivePanel(p)}
            className="px-3 py-1 rounded-full text-sm transition-colors"
            style={{
              background: activePanel === p ? 'var(--color-primary)' : 'var(--color-card)',
              color: activePanel === p ? '#fff' : 'var(--color-fg)',
              border: '1px solid var(--color-border)',
            }}
          >
            {p}
          </button>
        ))}
      </div>
      <div
        className="rounded-xl p-6 min-h-[300px]"
        style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}
      >
        {activePanel === 'System Health' ? (
          <div>
            <button
              onClick={checkHealth}
              className="px-4 py-2 rounded-lg font-medium mb-4"
              style={{ background: 'var(--color-primary)', color: '#fff' }}
            >
              Check Backend Health
            </button>
            {healthStatus && (
              <pre className="mt-2 p-3 rounded" style={{ background: 'var(--color-bg)' }}>
                {JSON.stringify(healthStatus, null, 2)}
              </pre>
            )}
          </div>
        ) : (
          <>
            <p className="opacity-60">Panel: {activePanel}</p>
            <div>Stub</div>
          </>
        )}
      </div>
    </div>
  );
}
