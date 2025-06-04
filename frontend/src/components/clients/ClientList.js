import React from 'react';
import axios from 'axios';

const ClientList = ({ clients, onClientDeleted }) => {
  const deleteClient = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/clients/${id}`);
      onClientDeleted(); // Llama a la función para actualizar la lista de clientes
    } catch (error) {
      console.error('Error deleting client:', error);
    }
  };

  return (
    <div>
      <h2>Client List</h2>
      <ul>
        {clients.map(client => (
          <li key={client.id}>
            {client.nombres} {client.apellidos} - {client.correo}
            <button onClick={() => deleteClient(client.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ClientList;
