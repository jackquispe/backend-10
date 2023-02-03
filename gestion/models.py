from django.db import models

class CategoriaModel(models.Model):
    # Si no especificamos la columna ID django lo harabde mamera 
    # predeterminada con el tipo de dato autofield y tmbn lo colcara como llave primnaria
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        # Sirve para defifnir los atributos de la clase que stamos heredadno
        # directamente para pasarle la metadata sin utilizar el metodo super
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        # sirve para modificar la configuracion y comportamiento de la base de la tabla
        # de la base de datos

        db_table = 'categorias'
        # modificamos el ordanamiento al momento de devolver los registros
        # nombre ascendente (A-Z)
        # nombre descendente (Z-A) USAMOS "[-nombre]"
        # para el ordenamiento es necesario que sean valore unicos
        ordering = ['nombre', 'id']

class PlatoModel(models.Model):
    # id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    # auto_now_add > cada vez que cree un nuevo registro su valor ser la hora y fecha actual
    # del servidor de base de datos.
    # db_column > indica como se quiere llamar esta columna en la base de datos
    fechaCreacion = models.DateField(auto_now_add=True, db_column='fecha_creacion')
    #Forma de indicar que accion debe tomar cuando se elimine el 'padre'
    # CASCADE >cuando se elimina la categoria en forma de cascada se eliminaran todos
    # PROTECT > Evita la eliminacion de la categoria si esta tiene platos que dependan de ella, aviso ProtectedError
    # RESTRICT > Restringe la eliminacion, es lo mismo que el protect, enviara un error RestrictedError
    # SET_NULL > Permite la eliminacion de la categoria y a los platos que dependan de ella les cambia su valor por NULL
    # SET_DEFAULT > permite eliminar la categoria y cambia su valor por defecto
    # DO_NOTHING > permite la eliminacion pero no hace nada ose mantiene el mismo numero de categoria en el plato a pesar
    # que esta no existe generando un problema de integridad
    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id')

    class Meta:
        db_table = 'platos'

