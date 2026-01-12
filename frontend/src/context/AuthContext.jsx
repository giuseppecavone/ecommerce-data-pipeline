import { createContext, useState, useContext, useEffect } from 'react';
import api from '../api/axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Al caricamento dell'app, controlliamo se c'è un token salvato
  useEffect(() => {
    const token = localStorage.getItem('token');
    const storedUser = localStorage.getItem('user');
    
    if (token && storedUser) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, []);

  // Funzione per gestire il Login
  const login = async (username, password) => {
    try {
      const response = await api.post('/login', { username, password });
      
      if (response.data.status === 'success') {
        const userData = { username: username }; // Potresti aggiungere altri dati dal backend
        
        // Salviamo nel localStorage per far durare la sessione
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', JSON.stringify(userData));
        
        setUser(userData);
        return { success: true };
      }
      return { success: false, message: response.data.message };
    } catch (error) {
      return { 
        success: false, 
        message: error.response?.data?.message || 'Errore di connessione' 
      };
    }
  };

  // Funzione per il Logout
  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

// Hook personalizzato per usare il contesto velocemente
export const useAuth = () => useContext(AuthContext);