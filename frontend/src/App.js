import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductList from './components/products/ProductList';
import ProductForm from './components/products/ProductForm';

const App = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://localhost:8000/products/');
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleProductAdded = () => {
    fetchProducts(); // Recargar la lista de productos
  };

  return (
    <div>
      <h1>Product Management</h1>
      <ProductForm onProductAdded={handleProductAdded} />
      <ProductList products={products} onProductDeleted={fetchProducts} />
    </div>
  );
};

export default App;
