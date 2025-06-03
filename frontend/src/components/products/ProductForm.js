import React, { useState } from 'react';
import axios from 'axios';
import './ProductForm.css'; // Importa el archivo CSS

const ProductForm = ({ onProductAdded }) => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    stock: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/products/', formData);
      onProductAdded();
      setFormData({
        name: '',
        description: '',
        price: '',
        stock: ''
      });
    } catch (error) {
      console.error('Error adding product:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <div>
        <label>
          Name:
          <input name="name" type="text" value={formData.name} onChange={handleChange} required />
        </label>
      </div>
      <div>
        <label>
          Description:
          <input name="description" type="text" value={formData.description} onChange={handleChange} required />
        </label>
      </div>
      <div>
        <label>
          Price:
          <input name="price" type="number" value={formData.price} onChange={handleChange} required />
        </label>
      </div>
      <div>
        <label>
          Stock:
          <input name="stock" type="number" value={formData.stock} onChange={handleChange} required />
        </label>
      </div>
      <button type="submit">Add Product</button>
    </form>
  );
};

export default ProductForm;
