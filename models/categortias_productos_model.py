from configuracion import conexion
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey

class Categoria_Prodcuto(conexion.Model):
    id = Column(type_= types.Integer, primary_key=True, autoincrement=True)
    
    # Foreignkey > me permite indicar que esta colkumna sera parte de 
    # relacion entre otra tabla

    categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer, nullable=False, name = 'categoria_id')
    productoId = Column(ForeignKey(column='productos.id'), type_=types.Integer, nullable=False, name = 'producto_id')

    __tablename__= 'categorias_productos'
