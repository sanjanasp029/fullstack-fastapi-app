import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../api/client';
import { useCart } from '../context/CartContext';

export default function ProductDetails() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const { refreshCart } = useCart();

  useEffect(() => {
    api.get(`/products/${id}`).then((res) => setProduct(res.data)).catch(() => setProduct(null));
  }, [id]);

  const addToCart = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      window.location.href = '/login';
      return;
    }
    await api.post('/cart', { product_id: Number(id), quantity: 1 });
    refreshCart();
  };

  if (!product) return <div className="container py-5">Loading...</div>;

  return (
    <div className="container py-5 product-detail">
      <div className="product-detail-grid">
        <img src={product.image_url || 'https://images.unsplash.com/photo-1551024601-bec78aea704b'} alt={product.name} />
        <div>
          <p className="eyebrow">{product.name}</p>
          <h2>{product.name}</h2>
          <div className="price-row"><strong>${product.price}</strong>{product.original_price && <span>${product.original_price}</span>}</div>
          <p>{product.description}</p>
          <div className="chip-row">
            <span>Stock: {product.stock}</span>
            <span>Rating: {product.rating}</span>
          </div>
          <button className="primary-btn" onClick={addToCart}>Add to cart</button>
          <Link className="secondary-btn" to="/shop">Continue shopping</Link>
        </div>
      </div>
    </div>
  );
}
