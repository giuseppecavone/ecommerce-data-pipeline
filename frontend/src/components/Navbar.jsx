import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, User, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm py-3">
      <div className="container">
        <Link className="navbar-brand fw-bold" to="/">🚀 INFINITY TECH</Link>
        
        <div className="d-flex align-items-center gap-3">
          <Link to="/cart" className="btn btn-outline-light position-relative">
            <ShoppingCart size={20} />
            {/* Qui aggiungeremo il badge del carrello più avanti */}
          </Link>

          {user ? (
            <div className="dropdown">
              <button className="btn btn-primary dropdown-toggle d-flex align-items-center gap-2" type="button" data-bs-toggle="dropdown">
                <User size={18} /> Profilo
              </button>
              <ul className="dropdown-menu dropdown-menu-end">
                <li><button className="dropdown-item d-flex align-items-center gap-2" onClick={handleLogout}>
                  <LogOut size={16} /> Esci
                </button></li>
              </ul>
            </div>
          ) : (
            <Link to="/login" className="btn btn-primary">Accedi</Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;