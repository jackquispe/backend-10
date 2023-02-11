import conexion from '../conector_bd.js'

export const crearProducto = async (req,res) => {
    const { body } = req
    // {nombre: 'blbla', precio:10, tieneIgv-, true, sku: '10a15, categoria_id: 1'}

    // primero buscar si existe la categoria
    const categoria = await conexion.categoria.findFirst({ where: { id:+body.categoriaId }})
    if(!categoria){
        return res.json({
            message: 'La categoria no existe',
        })
    }

    const respuesta = await conexion.producto.create({
        data: {
            // spread operator > sacar el contenido de un json, es decir utiliozare solo su contenido
            // mas no creae una llave llamada 'body'
            ...body,
            categoriaId: +body.categoriaId,
        },
    })

    res.json({
        message: 'producto creado exitosamente',
        content: respuesta,
    })

    // si no existe retornar un menaje que los datos son incorrecvtos

    // si existe la categoria entonces crear ese nuevo producto
}

export const toggleProducto = async (req,res) => {
    // habilitar - desabilitar el producto
    const { id } = req.params
    //SELECT habilitado FROM productos WHERE id = ...
    const producto = await conexion.producto.findFirst({
        where: {
            id: +id,
        },
        select:{
            habilitado: true,
        }
    })

    if(!producto){
        return res.json({
            message: 'El producto no existe'
        })
    }

    // !boolean > indicando que queremos el valor contrario
    const resultado = await conexion.producto.update({
        where: { id:+id },
        data:{
            habilitado: !producto.habilitado,
        },
        // select > se usa para retornar solo las columnas o campos que se necesitan, 
        // si no se coloca retornara todos los campos
        select:{
            habilitado: true, // aqui se indica que columnas queremos visualizar
        },
    })

    return res.json({
        message:'Producto ' + (resultado.habilitado === true ? 'habilitado': 'deshabilitado'),
    })
}