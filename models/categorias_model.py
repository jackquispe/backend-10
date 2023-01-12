from configuracion import conexion
from sqlalchemy import Column, types

class Categoria(conexion.Model):
    # Estamos indicando que esta clase se comportara ademas
    # como si fuera una tabla en la base de datos
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types
    id = Column(type_= types.Integer, autoincrement= True, primary_key=True)
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types
    nombre = Column(type_= types.String(length=45), nullable=False, unique=True)

    # indicar comoi se llamara la tabla en la base de datos
    __tablename__= 'categorias'