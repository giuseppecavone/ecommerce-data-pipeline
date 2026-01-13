import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, User, LogOut, Package } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const cartCount = 0;
  
  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm py-2 mb-4">
      <div className="container">
        {/* Logo con icona */}
        <Link className="navbar-brand d-flex align-items-center gap-2 fw-bold" to="/">
          <span style={{ fontSize: '1.5rem' }}>🚀</span> 
          <span className="d-none d-sm-inline">INFINITY TECH</span>
        </Link>

        {/* Gruppo icone e azioni */}
        <div className="d-flex align-items-center gap-2 gap-md-3">
          
          {/* Carrello */}
          <Link to="/cart" className="btn btn-link text-white position-relative p-2">
            <ShoppingCart size={22} />
        {cartCount > 0 && (
        <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" style={{ fontSize: '0.7rem' }}>
          {cartCount}
        </span>
      )}
    </Link>

          {user ? (
            <div className="dropdown">
              <button 
                className="btn btn-outline-light dropdown-toggle d-flex align-items-center gap-2 rounded-pill px-3" 
                type="button" 
                id="userDropdown"
                data-bs-toggle="dropdown" 
                aria-expanded="false"
              >
                <User size={18} /> 
                <span className="d-none d-md-inline">{user.username}</span>
              </button>
              <ul className="dropdown-menu dropdown-menu-end shadow-lg border-0 mt-2" aria-labelledby="userDropdown">
                <li className="px-3 py-2 small text-muted border-bottom mb-2">Account: {user.email}</li>
                <li>
                  <Link className="dropdown-item d-flex align-items-center gap-2" to="/orders">
                    <Package size={16} /> I miei ordini
                  </Link>
                </li>
                <li><hr className="dropdown-divider" /></li>
                <li>
                  <button className="dropdown-item d-flex align-items-center gap-2 text-danger" onClick={handleLogout}>
                    <LogOut size={16} /> Esci
                  </button>
                </li>
              </ul>
            </div>
          ) : (
            <Link to="/login" className="btn btn-primary rounded-pill px-4 fw-bold shadow-sm">
              Accedi
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;