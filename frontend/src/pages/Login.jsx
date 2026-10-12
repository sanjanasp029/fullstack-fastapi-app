import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/client';

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: '', password: '' });
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('/auth/login', form);
      localStorage.setItem('token', res.data.access_token);
      navigate('/');
    } catch (err) {
      setError('Invalid login details');
    }
  };

  return (
    <div className="auth-box container">
      <h2>Login</h2>
      {error && <div className="alert">{error}</div>}
      <form onSubmit={handleSubmit} className="stack-form">
        <input type="email" placeholder="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
        <input type="password" placeholder="Password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} />
        <button className="primary-btn" type="submit">Login</button>
      </form>
    </div>
  );
}
