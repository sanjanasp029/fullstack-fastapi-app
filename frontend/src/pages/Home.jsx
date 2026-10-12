import { useEffect, useState } from 'react';
import api from '../api/client';

export default function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get('/products').then((res) => setProducts(res.data.slice(0, 4))).catch(() => setProducts([]));
  }, []);

  return (
    <>
      <section className="hero-section">
        <div className="container hero-grid">
          <div>
            <span className="eyebrow">Handcrafted luxury</span>
            <h1>Chocolate made to delight every moment.</h1>
            <p>Discover premium dark, milk, white chocolates and curated gift assortments for every occasion.</p>
            <div className="hero-actions">
              <a className="primary-btn" href="/shop">Shop now</a>
              <a className="secondary-btn" href="/admin">Admin</a>
            </div>
          </div>
          <div className="hero-card">
            <img src="https://images.unsplash.com/photo-1511381939415-e44015466834" alt="Chocolate" />
          </div>
        </div>
      </section>

      <section className="container py-5">
        <div className="section-head">
          <h2>Featured chocolates</h2>
          <a href="/shop">View all</a>
        </div>
        <div className="product-grid">
          {products.map((product) => (
            <div key={product.id} className="product-card">
              <img src={product.image_url || 'https://images.unsplash.com/photo-1551024601-bec78aea704b'} alt={product.name} />
              <div className="product-body">
                <h4>{product.name}</h4>
                <p>{product.description}</p>
                <div className="price-row">
                  <strong>${product.price}</strong>
                </div>
                <a href={`/product/${product.id}`} className="primary-btn small">View details</a>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
