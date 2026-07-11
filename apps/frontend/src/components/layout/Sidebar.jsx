import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  Users,
  Briefcase,
  HardHat,
  Bot,
  Settings,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react';

const navItems = [
  { to: '/', label: 'Overview', icon: LayoutDashboard },
  { to: '/hr', label: 'HR Portal', icon: Users },
  { to: '/sales', label: 'Sales & CRM', icon: Briefcase },
  { to: '/operations', label: 'Operations', icon: HardHat },
  { to: '/ai', label: 'AI Assistant', icon: Bot },
  { to: '/settings', label: 'Settings', icon: Settings },
];

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <aside
      className="flex flex-col border-r transition-all duration-300"
      style={{
        width: collapsed ? '64px' : '240px',
        background: 'var(--color-card)',
        borderColor: 'var(--color-border)',
      }}
    >
      <div className="flex items-center justify-between p-4">
        {!collapsed && <span className="text-lg font-bold">ERP</span>}
        <button onClick={() => setCollapsed(!collapsed)} className="p-1 rounded hover:opacity-70">
          {collapsed ? <ChevronRight size={20} /> : <ChevronLeft size={20} />}
        </button>
      </div>
      <nav className="flex-1 flex flex-col gap-1 px-2">
        {navItems.map(({ to, label, icon: Icon }) => (
          <NavLink
            key={to}
            to={to}
            end={to === '/'}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${
                isActive ? 'font-semibold' : 'opacity-70 hover:opacity-100'
              }`
            }
            style={({ isActive }) => ({
              background: isActive ? 'var(--color-primary)' : 'transparent',
              color: isActive ? '#fff' : 'var(--color-fg)',
            })}
          >
            <Icon size={20} />
            {!collapsed && <span>{label}</span>}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
