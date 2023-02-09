from django.contrib.auth.models import BaseUserManager
# BaseUserManager > sirve para modificar la creacion y admnistracion de los auth_user

class UsuarioManager(BaseUserManager):
    # esta clase me permite modificar la administracion del usuario mediante el comando createsuperuser
    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password):
        # valido si es que no hay correo
        if not correo:
            raise ValueError("El usuario no proporciono el correo")
        # valido que el correo cumpla el formato correcto
        # removera los espacios al inicio y al final y validara que no utlice caracteres incorrectos
        correo_normalizado = self.normalize_email(correo)
        # llamamos al modelo que estamos utilizando e inicializando el nuevo usuario
        nuevo_usuario = self.model(correo=correo_normalizado, nombre=nombre, apellido=apellido, tipoUsuario=tipoUsuario)

        # generamos el hash de la contraseña
        # generar el hash de la contraseña utilizando algoritmos de hash SHA512
        # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()