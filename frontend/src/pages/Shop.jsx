import { useEffect, useState } from 'react';
import api from '../api/client';
import ProductCard from '../components/ProductCard';

export default function Shop() {
  const [products, setProducts] = useState([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    api.get('/products').then((res) => setProducts(res.data)).catch(() => setProducts([]));
  }, []);

  const filtered = products.filter((p) => p.name.toLowerCase().includes(query.toLowerCase()));

  return (
    <div className="container py-5">
      <div className="shop-header">
        <h2>Shop premium chocolates</h2>
        <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search chocolates" className="search-input" />
      </div>
      <div className="product-grid">
        {filtered.map((product) => (
          <ProductCard product={product} key={product.id} />
        ))}
      </div>
    </div>
  );
}
