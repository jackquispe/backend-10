from flask_restful import Resource, request   # permite trabajr con clases
from configuracion import conexion
from models.categorias_model import Categoria
from dtos.categoria_dto import CategoriaDto
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError

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
        data = request.get_json()
        print (data)
        serializador = CategoriaDto()
        try:

            # load> valida el diccionario que cumpla con todas las caracteristicas de las
            # columnas de nuestro modelo y si es devolvera un diccionario con al informaicon necesaria
            resultado = serializador.load(data)
            print(resultado)
            # Inicializamos nuestra categoria pero aun no lo guardamos
            nuevaCategoria = Categoria(nombre = resultado.get('nombre'))
            # Agregamos este nuevo elemento a la base de datos
            conexion.session.add(nuevaCategoria)
            # Indicamos que se guarde de manera permanente
            conexion.session.commit()

            return {
                'message': 'Categoria creada exitosamente'
            }
        except IntegrityError as error_integridad:
            # Aca se ingresara si al momento de guardar la categoria ya existe
            return {
                'message': 'Error al crear la categoria, esa catefgoria ya existe'
            }
        except ValidationError as error_validacion:
            # Aca se ingresara cuando nos de un error de la validqacion del dto
            return{
                'message': 'Error al crear la categoria, vea el content',
                'content': error_validacion.args
            }
        except Exception as error:
            # Aca ingresara si el error es un error que no cumple con los anteriores errores
            return{
                'message': 'Error al crear la categoria',
                'content': error.args # aqui es donde almacenan todos los mensajes de error
            }

class CategoriaController(Resource):
    def get(self, id):
        print(id)
        # SELECT * FROM categorias WHERE id = ....LIMIT 1;
        categoria = conexion.session.query(Categoria).filter_by(id=id).first()
        print(categoria)
        # TODO: comnvertir esta categoria para mostrar en el content, si l acategoria no existe
        # indicar que la categoria no existe en el 'message'
        return {
            'content': ''
        }