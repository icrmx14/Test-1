import { useState } from 'react';

const sections = [
  'SKU Tracker',
  'Categories',
  'Batch / Serial Numbers',
  'Reorder Points',
  'Stock Adjustments',
  'Multi-Warehouse',
  'Stock Transfers',
  'Employee Allocation',
  'Machine Allocation',
  'Booking Calendars',
  'Equipment Tracking',
  'Maintenance Schedules',
  'Warranty / Depreciation',
  'Kanban Board',
  'Gantt Chart',
  'Timesheets',
  'Billable Hours',
  'BOM Canvas',
  'Work Orders',
  'Quality Inspection',
  'Risk / Compliance',
];

export default function Operations() {
  const [activeSection, setActiveSection] = useState(sections[0]);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Logistics, Projects & Operations</h2>
      <div className="flex flex-wrap gap-2 mb-6">
        {sections.map(s => (
          <button
            key={s}
            onClick={() => setActiveSection(s)}
            className="px-3 py-1 rounded-full text-sm transition-colors"
            style={{
              background: activeSection === s ? 'var(--color-primary)' : 'var(--color-card)',
              color: activeSection === s ? '#fff' : 'var(--color-fg)',
              border: '1px solid var(--color-border)',
            }}
          >
            {s}
          </button>
        ))}
      </div>
      <div
        className="rounded-xl p-6 min-h-[300px]"
        style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}
      >
        <p className="opacity-60">Section: {activeSection}</p>
        <div>Stub</div>
      </div>
    </div>
  );
}
