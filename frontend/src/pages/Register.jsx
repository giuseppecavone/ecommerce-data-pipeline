import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom'; // Scommentato
import axios from 'axios';

const Register = () => {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/register', formData);
      if (response.data) {
        alert("Registrazione completata!");
        navigate('/login');
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Errore durante la registrazione');
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: '400px' }}>
      <div className="card shadow p-4 border-0">
        <h2 className="text-primary text-center mb-4">Crea Account</h2>
        
        {error && <div className="alert alert-danger">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Username</label>
            <input 
              type="text" 
              className="form-control" 
              value={formData.username}
              onChange={(e) => setFormData({...formData, username: e.target.value})} 
              required 
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Email</label>
            <input 
              type="email" 
              className="form-control" 
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})} 
              required 
            />
          </div>
          <div className="mb-4">
            <label className="form-label">Password</label>
            <input 
              type="password" 
              className="form-control" 
              value={formData.password}
              onChange={(e) => setFormData({...formData, password: e.target.value})} 
              required 
            />
          </div>
          <button type="submit" className="btn btn-primary w-100 py-2">Registrati</button>
        </form>
        
        <p className="mt-3 text-center">
          Hai già un account? <Link to="/login">Accedi qui</Link>
        </p>
      </div>
    </div>
  );
};

export default Register;