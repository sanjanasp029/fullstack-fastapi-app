import { useEffect, useState } from 'react';
import api from '../api/client';

export default function AdminDashboard() {
  const [summary, setSummary] = useState({ total_sales: 0, total_orders: 0, total_customers: 0, total_products: 0, low_stock: 0 });

  useEffect(() => {
    api.get('/admin/summary').then((res) => setSummary(res.data)).catch(() => setSummary({ total_sales: 0, total_orders: 0, total_customers: 0, total_products: 0, low_stock: 0 }));
  }, []);

  return (
    <div className="container py-5">
      <h2>Admin dashboard</h2>
      <div className="stats-grid">
        <div className="stat-box"><span>Total sales</span><strong>${summary.total_sales}</strong></div>
        <div className="stat-box"><span>Total orders</span><strong>{summary.total_orders}</strong></div>
        <div className="stat-box"><span>Customers</span><strong>{summary.total_customers}</strong></div>
        <div className="stat-box"><span>Low stock</span><strong>{summary.low_stock}</strong></div>
      </div>
    </div>
  );
}
