import { useContext } from 'react';
import { Sun, Moon, Bell, UserCircle } from 'lucide-react';
import ThemeContext from '../../context/ThemeContext';

export default function Header() {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <header
      className="flex items-center justify-between px-6 py-3 border-b"
      style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}
    >
      <h1 className="text-xl font-semibold">AI-Powered ERP</h1>
      <div className="flex items-center gap-4">
        <button onClick={toggleTheme} className="p-2 rounded-lg hover:opacity-70" title="Toggle theme">
          {theme === 'light' ? <Moon size={20} /> : <Sun size={20} />}
        </button>
        <button className="relative p-2 rounded-lg hover:opacity-70" title="Notifications">
          <Bell size={20} />
          <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-red-500" />
        </button>
        <button className="p-2 rounded-lg hover:opacity-70" title="Profile">
          <UserCircle size={24} />
        </button>
      </div>
    </header>
  );
}
