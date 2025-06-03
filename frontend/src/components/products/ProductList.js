import React from 'react';
import axios from 'axios';

const ProductList = ({ products, onProductDeleted }) => {
  const deleteProduct = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/products/${id}`);
      onProductDeleted(); // Llama a la función para actualizar la lista de productos
    } catch (error) {
      console.error('Error deleting product:', error);
    }
  };

  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            {product.name} - {product.description} - {product.price}
            <button onClick={() => deleteProduct(product.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
