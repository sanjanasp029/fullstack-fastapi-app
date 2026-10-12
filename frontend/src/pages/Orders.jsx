import { useEffect, useState } from 'react';
import api from '../api/client';

export default function Orders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api.get('/orders').then((res) => setOrders(res.data)).catch(() => setOrders([]));
  }, []);

  return (
    <div className="container py-5">
      <h2>My orders</h2>
      {orders.length === 0 ? <p>No orders yet.</p> : orders.map((order) => (
        <div className="order-card" key={order.id}>
          <h4>{order.order_number}</h4>
          <p>Status: {order.status}</p>
          <p>Total: ${order.total}</p>
        </div>
      ))}
    </div>
  );
}
