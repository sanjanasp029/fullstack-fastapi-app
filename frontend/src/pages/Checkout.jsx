import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/client';

export default function Checkout() {
  const navigate = useNavigate();
  const [shippingAddress, setShippingAddress] = useState('123 Cocoa Lane, New York, NY');
  const [paymentMethod, setPaymentMethod] = useState('Card');
  const [notes, setNotes] = useState('');

  const handleCheckout = async () => {
    await api.post('/orders', {
      shipping_address: shippingAddress,
      payment_method: paymentMethod,
      notes,
    });
    navigate('/orders');
  };

  return (
    <div className="container py-5 checkout-box">
      <h2>Checkout</h2>
      <label>Shipping address</label>
      <textarea value={shippingAddress} onChange={(e) => setShippingAddress(e.target.value)} />
      <label>Payment method</label>
      <select value={paymentMethod} onChange={(e) => setPaymentMethod(e.target.value)}>
        <option value="Card">Card</option>
        <option value="Cash on Delivery">Cash on Delivery</option>
      </select>
      <label>Order notes</label>
      <textarea value={notes} onChange={(e) => setNotes(e.target.value)} />
      <button className="primary-btn" onClick={handleCheckout}>Place order</button>
    </div>
  );
}
