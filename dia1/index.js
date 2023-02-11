// Asi se importa utilizando ECMAScript
import express from 'express'

import { crearCategoria, listarCategorias, buscarCategoriaPorId, actualizarCategoria, eliminarCategoria } from './controllers/categorias.controller.js'

import { productoRouter } from './routes/productos.routes.js';

// Asi se importa utlizando CommonJs
// const express = require("express");
// const { PrismaClient } = require("@prisma/client")
// const { crearCategoria } = require('./controllers/categorias.controller')



// se va a copiar toda la funcionalidad de la loiberia express en la variable servidor 
const servidor = express()

// que ahora mi servidor podra convertir la info entrante para los json
// middleware para comnvertir la informacion entrante a un formato legible
servidor.use(express.json())

servidor.get('/', (req,res)=>{
    // req > es la informacion que me emvia el cliente
    // res > es la informacion que voy a devolver al cliente
    res.json({
        message: "Bienvenido a mi API",
    });
});

servidor.use(productoRouter)

servidor.route('/categorias').post(crearCategoria).get(listarCategorias)
servidor.route('/categorias/:id').get(buscarCategoriaPorId).put(actualizarCategoria).delete(eliminarCategoria)

servidor.post("/productos", (req,res)=>{
    console.log(req.body);

    res.json({
        message: "Producto creado exitosamente",
    });
});

servidor.listen(5000, ()=>{
    console.log('Servidor corriendo exitosamente en el puerto 5000');
});
