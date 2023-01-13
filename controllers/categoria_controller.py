from flask_restful import Resource
from configuracion import conexion
from models.categorias_model import Categoria
from dtos.categoria_dto import CategoriaDto

# ahora en esta clase pdore utilizar los metodos HTTP  (GET, POST, PUT, DELETE) como
# si fuesen metodos de la clase
class CategoriasController(Resource):
    def get(self):
        # SELECT * FROM categorias
        data = conexion.session.query(Categoria).all()
        print(data[0].nombre) 
        # manu=True > indicando que le vamos a pasar una loista de instancias
        # y el dto la tendra que iterar para poder convertir cada una de ellas
               
        serializador = CategoriaDto(many=True)
        #dump > convierte la instancia de la clase a un diccionario
        resultado = serializador.dump(data)
        return {
            'content': resultado
        }
    
    def post(self):
        return {
            'message': 'me hiciste post'
        }