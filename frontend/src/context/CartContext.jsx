import { createContext, useContext, useEffect, useState } from 'react';
import api from '../api/client';

const CartContext = createContext();

export function CartProvider({ children }) {
  const [cart, setCart] = useState({ items: [], subtotal: 0, total: 0 });

  const refreshCart = async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        setCart({ items: [], subtotal: 0, total: 0 });
        return;
      }
      const res = await api.get('/cart');
      setCart(res.data);
    } catch (err) {
      setCart({ items: [], subtotal: 0, total: 0 });
    }
  };

  useEffect(() => { refreshCart(); }, []);

  return <CartContext.Provider value={{ cart, refreshCart }}>{children}</CartContext.Provider>;
}

export const useCart = () => useContext(CartContext);
