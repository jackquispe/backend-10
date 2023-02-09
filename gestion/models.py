from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager

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
   
    # related_name > sirve para poder acceder a todos los regostros desde la otra entidad, es decir desde categoria poder acceder a 
    # todos sus platos, si es que no se define su valor sera puesto por djangho con el nombre de la clase "todo en minusculas", seguido
    # de la palbra "_set" 'platomodel_set'
    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='platos')

    class Meta:
        db_table = 'platos'


# como vamos a modificarel comportamiento de la tabla auth_user de django entonces tenemos
# que modificar su herencia
class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    # PermissionsMixin > sirve para poder relacionar la tabla auth_user con las demas tablas de permisos
    # tanto la de auth_permission como la de group_permissions

    # AbstractBaseUser > me permite modificar todo lo que yo quiera del metodo auth_user
    # mientras que AbtractUser solamente me permite agregar nuevas columnas
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    # django hace una validacion para que el correo cumpla con el fomrato valido
    # xxxx@xxxx.xxx
    correo = models.EmailField(max_length=100, unique=True)
    password = models.TextField(null=False)
    # choices (opciones) > tiene dos nombres, el primero se guardara en la base de datos
    # # el segudno es el que se mostrara al momento de devolver la informacion 
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'),
        ('MOZO', 'MOZO'),
        ('CLIENTE', 'CLIENTE')
    ])
    # propiedades netas para el panel administrativo(solo si se va a trabajar con el panel administrativo)
    # is_staff > sirve para indicar si el usuario que quiere acceder pertenece o no al equipo
    is_staff = models.BooleanField(default=False)
    # is_active > sirve para indicar si el usuario es un usuario activo de la empresa
    is_active = models.BooleanField(default=True)
    # createdAt > sirve para indicar la fecha en la que se creo el usuario
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
    # se utilizar para el panel administrativo para indicar cual es el atributo que debe pedir como nombre de usuario
    USERNAME_FIELD = 'correo'

    # son las columnas o los atributos requeridos al momento de crear el superusuario por consola, no se coloca
    # el username_field ni tampoco la contraseña porque ya son implicitos
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

    objects = UsuarioManager()
    class Meta:
        db_table = 'usuarios'