// Kumara Fawwas Abhista
// 2200016100
// Kelas C

const express = require('express');
const app = express();
const port = 3000;

const controller = require('./controller');

app.use(express.json());


app.get('/api/items', controller.getItems);  
app.post('/api/items', controller.createItem); 
app.put('/api/items/:id', controller.updateItem); 
app.delete('/api/items/:id', controller.deleteItem); 

app.listen(port, () => { 
    console.log(`API is running on http://localhost:${port}`);
});

module.exports = app;