import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <header className="topbar">
      <div className="container nav-row">
        <Link to="/" className="brand">Cocoa Luxe</Link>
        <nav className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/shop">Shop</Link>
          <Link to="/orders">Orders</Link>
          {user?.is_admin && <Link to="/admin">Admin</Link>}
        </nav>
        <div className="nav-actions">
          {user ? (
            <>
              <span>{user.name}</span>
              <button className="nav-btn" onClick={logout}>Logout</button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
          <Link to="/cart" className="cart-pill">Cart</Link>
        </div>
      </div>
    </header>
  );
}
