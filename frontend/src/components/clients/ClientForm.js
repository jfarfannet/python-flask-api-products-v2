import React, { useState } from 'react';
import axios from 'axios';
import './ClientForm.css'; // Asegúrate de tener un archivo CSS similar para los estilos

const ClientForm = ({ client, onClientAdded }) => {
  const [formData, setFormData] = useState({
    nombres: client ? client.nombres : '',
    apellidos: client ? client.apellidos : '',
    correo: client ? client.correo : ''
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
      if (client) {
        await axios.put(`http://localhost:8000/clients/${client.id}`, formData);
      } else {
        await axios.post('http://localhost:8000/clients/', formData);
      }
      onClientAdded(); // Llama a la función para actualizar la lista de clientes
      setFormData({
        nombres: '',
        apellidos: '',
        correo: ''
      }); // Limpia el formulario
    } catch (error) {
      console.error('Error saving client:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <div>
        <label>
          Nombres:
          <input name="nombres" type="text" value={formData.nombres} onChange={handleChange} required />
        </label>
      </div>
      <div>
        <label>
          Apellidos:
          <input name="apellidos" type="text" value={formData.apellidos} onChange={handleChange} required />
        </label>
      </div>
      <div>
        <label>
          Correo:
          <input name="correo" type="email" value={formData.correo} onChange={handleChange} required />
        </label>
      </div>
      <button type="submit">Save Client</button>
    </form>
  );
};

export default ClientForm;
