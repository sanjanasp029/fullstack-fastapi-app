export default function ProductCard({ product }) {
  return (
    <div className="product-card">
      <img src={product.image_url || 'https://images.unsplash.com/photo-1551024601-bec78aea704b'} alt={product.name} />
      <div className="product-body">
        <h4>{product.name}</h4>
        <p>{product.description}</p>
        <div className="price-row">
          <strong>${product.price}</strong>
          {product.original_price && <span>${product.original_price}</span>}
        </div>
        <a href={`/product/${product.id}`} className="primary-btn small">View</a>
      </div>
    </div>
  );
}
