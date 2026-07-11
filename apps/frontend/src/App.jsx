import React, { useState, useEffect } from 'react';
import { LayoutDashboard, Boxes, TrendingUp, RefreshCw, Plus, Package } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('inventory'); // Standard default to work on inventory
  const [backendStatus, setBackendStatus] = useState({ loading: true, online: false });
  const [products, setProducts] = useState([]);
  const [showModal, setShowModal] = useState(false);
  
  // Form State
  const [formData, setFormData] = useState({ sku: '', name: '', category: '', price: '', current_stock: '' });

  const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

  const fetchProducts = () => {
    fetch(`${API_URL}/api/v1/inventory/`)
      .then((res) => {
        if (res.ok) return res.json();
        throw new Error();
      })
      .then((data) => {
        setProducts(data);
        setBackendStatus({ loading: false, online: true });
      })
      .catch(() => {
        setBackendStatus({ loading: false, online: false });
      });
  };

  useEffect(() => {
    fetchProducts();
  }, [API_URL]);

  const handleCreateProduct = (e) => {
    e.preventDefault();
    fetch(`${API_URL}/api/v1/inventory/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...formData,
        price: parseFloat(formData.price),
        current_stock: parseInt(formData.current_stock, 10)
      })
    })
    .then((res) => {
      if(res.ok) {
        setShowModal(false);
        setFormData({ sku: '', name: '', category: '', price: '', current_stock: '' });
        fetchProducts(); // Refresh list instantly
      } else {
        alert("Failed to create SKU. Check if it's unique.");
      }
    });
  };

  return (
    <div className="flex h-screen bg-slate-50 text-slate-800">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-900 text-white flex flex-col justify-between">
        <div className="p-6">
          <h1 className="text-xl font-bold tracking-wider text-indigo-400">📊 OptiDemand ERP</h1>
          <nav className="mt-8 space-y-2">
            <button onClick={() => setActiveTab('dashboard')} className={`w-full flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm ${activeTab === 'dashboard' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:bg-slate-800'}`}>
              <LayoutDashboard size={18} /> Dashboard
            </button>
            <button onClick={() => setActiveTab('inventory')} className={`w-full flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm ${activeTab === 'inventory' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:bg-slate-800'}`}>
              <Boxes size={18} /> Inventory Control
            </button>
            <button onClick={() => setActiveTab('forecasting')} className={`w-full flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm ${activeTab === 'forecasting' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:bg-slate-800'}`}>
              <TrendingUp size={18} /> AI Forecasting
            </button>
          </nav>
        </div>

        <div className="p-4 bg-slate-950 text-xs flex items-center justify-between">
          <span>Engine:</span>
          {backendStatus.online ? <span className="text-emerald-400 font-semibold">● Online</span> : <span className="text-rose-400 font-semibold">● Offline</span>}
        </div>
      </aside>

      {/* Main Panel */}
      <main className="flex-1 overflow-y-auto p-8">
        <header className="flex justify-between items-center mb-8">
          <div>
            <h2 className="text-2xl font-bold text-slate-900 capitalize">{activeTab} Control Hub</h2>
            <p className="text-sm text-slate-500">Live operational data flow tracking.</p>
          </div>
          {activeTab === 'inventory' && (
            <button onClick={() => setShowModal(true)} className="flex items-center gap-2 bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700 transition-colors">
              <Plus size={16} /> Add New SKU
            </button>
          )}
        </header>

        {activeTab === 'inventory' && (
          <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
            {products.length === 0 ? (
              <div className="text-center py-12">
                <Package className="mx-auto text-slate-300 mb-4" size={48} />
                <h3 className="text-lg font-medium">No Products Found</h3>
                <p className="text-slate-500 text-sm mt-1">Create your first product item using the action trigger above.</p>
              </div>
            ) : (
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="bg-slate-50 border-b border-slate-200 text-slate-400 text-xs font-semibold uppercase tracking-wider">
                    <th className="p-4">SKU Code</th>
                    <th className="p-4">Product Name</th>
                    <th className="p-4">Category</th>
                    <th className="p-4">Price</th>
                    <th className="p-4">Current Stock</th>
                    <th className="p-4">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 text-sm">
                  {products.map((p) => (
                    <tr key={p.id} className="hover:bg-slate-50/70 transition-colors">
                      <td className="p-4 font-mono font-semibold text-indigo-600">{p.sku}</td>
                      <td className="p-4 font-medium text-slate-900">{p.name}</td>
                      <td className="p-4 text-slate-500">{p.category}</td>
                      <td className="p-4 text-slate-600">${p.price.toFixed(2)}</td>
                      <td className="p-4 font-medium">{p.current_stock} units</td>
                      <td className="p-4">
                        {p.current_stock <= p.safety_stock ? (
                          <span className="bg-amber-50 text-amber-700 border border-amber-200 px-2.5 py-1 rounded-full text-xs font-medium">Low Stock</span>
                        ) : (
                          <span className="bg-emerald-50 text-emerald-700 border border-emerald-200 px-2.5 py-1 rounded-full text-xs font-medium">Optimal</span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        )}

        {/* Modal Overlay Component */}
        {showModal && (
          <div className="fixed inset-0 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-md p-6 border border-slate-100 animate-in fade-in zoom-in-95 duration-150">
              <h3 className="text-lg font-bold text-slate-900 mb-4">Register Catalog Product</h3>
              <form onSubmit={handleCreateProduct} className="space-y-4">
                <div>
                  <label className="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">SKU Unique Identifier</label>
                  <input type="text" required placeholder="e.g., APP-MAC-01" className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:outline-indigo-600" value={formData.sku} onChange={(e) => setFormData({...formData, sku: e.target.value.toUpperCase()})} />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">Product Title</label>
                  <input type="text" required placeholder="e.g., Apple MacBook Pro" className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:outline-indigo-600" value={formData.name} onChange={(e) => setFormData({...formData, name: e.target.value})} />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">Category Division</label>
                  <input type="text" required placeholder="e.g., Electronics" className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:outline-indigo-600" value={formData.category} onChange={(e) => setFormData({...formData, category: e.target.value})} />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">Unit Price ($)</label>
                    <input type="number" step="0.01" required placeholder="1299.99" className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:outline-indigo-600" value={formData.price} onChange={(e) => setFormData({...formData, price: e.target.value})} />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">Initial Volumetric Stock</label>
                    <input type="number" required placeholder="45" className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:outline-indigo-600" value={formData.current_stock} onChange={(e) => setFormData({...formData, current_stock: e.target.value})} />
                  </div>
                </div>
                <div className="flex justify-end gap-3 pt-4 border-t border-slate-100">
                  <button type="button" onClick={() => setShowModal(false)} className="px-4 py-2 text-sm text-slate-500 hover:bg-slate-50 rounded-lg">Cancel</button>
                  <button type="submit" className="px-4 py-2 text-sm bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 font-medium">Commit Product</button>
                </div>
              </form>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}