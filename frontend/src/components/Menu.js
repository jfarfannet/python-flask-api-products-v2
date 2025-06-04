import React from 'react';

const Menu = ({ onNavigate }) => {
  return (
    <nav>
      <button onClick={() => onNavigate('products')}>Products</button>
      <button onClick={() => onNavigate('clients')}>Clients</button>
    </nav>
  );
};

export default Menu;
