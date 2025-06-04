import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Menu from './components/Menu';
import ProductList from './components/products/ProductList';
import ProductForm from './components/products/ProductForm';
import ClientList from './components/clients/ClientList';
import ClientForm from './components/clients/ClientForm';

const App = () => {
  const [view, setView] = useState('products'); // Estado para manejar la vista actual
  const [products, setProducts] = useState([]);
  const [clients, setClients] = useState([]);

  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://localhost:8000/products/');
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  const fetchClients = async () => {
    try {
      const response = await axios.get('http://localhost:8000/clients/');
      setClients(response.data);
    } catch (error) {
      console.error('Error fetching clients:', error);
    }
  };

  useEffect(() => {
    fetchProducts();
    fetchClients();
  }, []);

  return (
    <div>
      <h1>Management System</h1>
      <Menu onNavigate={setView} />
      {view === 'products' && (
        <>
          <ProductForm onProductAdded={fetchProducts} />
          <ProductList products={products} onProductDeleted={fetchProducts} />
        </>
      )}
      {view === 'clients' && (
        <>
          <ClientForm onClientAdded={fetchClients} />
          <ClientList clients={clients} onClientDeleted={fetchClients} />
        </>
      )}
    </div>
  );
};

export default App;
