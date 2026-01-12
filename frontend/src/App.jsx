import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';



// Se hai creato anche il carrello, importalo qui

function App() {
  console.log("App caricata!");
  return (
    <Router>
      <div className="min-vh-100 bg-light">
        {/* La Navbar rimane fissa in alto su tutte le pagine */}
        <Navbar /> 
        
        {/* Qui cambiano i contenuti in base all'URL */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;