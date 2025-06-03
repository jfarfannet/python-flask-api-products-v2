import api from './api';

export const getClients = () => api.get('/clients/');
export const getClient = (id) => api.get(`/clients/${id}`);
export const createClient = (client) => api.post('/clients/', client);
export const updateClient = (id, client) => api.put(`/clients/${id}`, client);
export const deleteClient = (id) => api.delete(`/clients/${id}`);
