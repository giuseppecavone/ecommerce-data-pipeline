import { useEffect, useState } from 'react';
import api from '../api/axios';
import ProductCard from '../components/ProductCard';

const Home = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Funzione per recuperare i prodotti dal backend Flask
    const fetchProducts = async () => {
      try {
        setLoading(true);
        // Questa chiamata punta a http://localhost:5000/api/products grazie alla config di axios
        const response = await api.get('/products');
        setProducts(response.data);
        setLoading(false);
      } catch (err) {
        console.error("Errore nel caricamento prodotti:", err);
        setError("Impossibile caricare i prodotti. Assicurati che il backend sia attivo.");
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Caricamento...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger shadow-sm" role="alert">
          {error}
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5 pb-5">
      <div className="d-flex justify-content-between align-items-end mb-4">
        <div>
          <h1 className="fw-bold mb-0">Catalogo Prodotti</h1>
          <p className="text-muted">Scopri le nostre ultime offerte tecnologiche</p>
        </div>
        <span className="badge bg-secondary">{products.length} Prodotti trovati</span>
      </div>

      {products.length === 0 ? (
        <div className="text-center my-5 py-5 border rounded bg-white shadow-sm">
          <p className="text-muted h5">Nessun prodotto disponibile nel database.</p>
        </div>
      ) : (
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
          {products.map(product => (
            <div className="col" key={product.id}>
              <ProductCard product={product} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Home;