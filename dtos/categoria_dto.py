from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categorias_model import Categoria

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        # sirve para pasarle los metadatos a las clase que tasmos heredando en una clase
        # exclusiva de python
        # metadatos son informacion que necesita la clase que estamos heredando como
        # atributos para que pueda funcionar correctamenete
        # sirve para indicar mediante qlue modelo se tiene que guiar para
        # hacer el mapeo de la informaicon
        model = Categoria

