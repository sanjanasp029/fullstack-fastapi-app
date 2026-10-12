import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api/client';
import { useCart } from '../context/CartContext';

export default function Cart() {
  const { cart, refreshCart } = useCart();

  const removeItem = async (id) => {
    await api.delete(`/cart/${id}`);
    refreshCart();
  };

  return (
    <div className="container py-5">
      <h2>Your cart</h2>
      {cart.items.length === 0 ? (
        <div>
          <p>Your cart is empty.</p>
          <Link className="primary-btn" to="/shop">Continue shopping</Link>
        </div>
      ) : (
        <div className="cart-layout">
          <div className="cart-items">
            {cart.items.map((item) => (
              <div key={item.id} className="cart-item">
                <div>
                  <h4>{item.product_name}</h4>
                  <p>Quantity: {item.quantity}</p>
                  <p>Subtotal: ${item.subtotal}</p>
                </div>
                <button className="secondary-btn" onClick={() => removeItem(item.id)}>Remove</button>
              </div>
            ))}
          </div>
          <aside className="summary-box">
            <h3>Order summary</h3>
            <div className="summary-line"><span>Subtotal</span><strong>${cart.subtotal}</strong></div>
            <div className="summary-line"><span>Total</span><strong>${cart.total}</strong></div>
            <Link className="primary-btn" to="/checkout">Proceed to checkout</Link>
          </aside>
        </div>
      )}
    </div>
  );
}
