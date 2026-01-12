import { ShoppingCart, Tag } from 'lucide-react';

const ProductCard = ({ product }) => {
  return (
    <div className="card h-100 border-0 shadow-sm hover-shadow transition">
      <div className="card-body d-flex flex-column">
        <div className="d-flex justify-content-between align-items-start mb-2">
          <span className="badge bg-light text-dark border d-flex align-items-center gap-1">
            <Tag size={12} /> {product.category}
          </span>
        </div>
        <h5 className="card-title fw-bold text-dark">{product.name}</h5>
        <p className="card-text text-muted small flex-grow-1">
          {/* Qui potresti aggiungere una descrizione se presente nel DB */}
          Disponibilità immediata
        </p>
        <div className="mt-3 pt-3 border-top d-flex justify-content-between align-items-center">
          <span className="h5 mb-0 fw-bold text-primary">€{product.price.toFixed(2)}</span>
          <button className="btn btn-outline-primary btn-sm d-flex align-items-center gap-2 px-3">
            <ShoppingCart size={16} /> Aggiungi
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;