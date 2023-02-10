from rest_framework.permissions import BasePermission
from .models import UsuarioModel
class SoloAdministradores(BasePermission):
    # message > sirve para cambiar el emnsaje de error
    message = 'solamente los administradores pueden realizar esta accion'
    def has_permission(self, request, view):
        # request.user > me retorna el usuario registrado
        print(request.user)
        usuario:UsuarioModel = request.user
        # request.auth > me retorna el contexto que utilizo el usuario para la autenticacion token
        print(request.auth)

        print(usuario.tipoUsuario)

        if usuario.tipoUsuario == 'ADMINISTRADOR':
            return True
        else:
            return False
    
class SoloMozos(BasePermission):
    message = 'Solamente los mozos pueden utilizar esta accion'

    def has_permission(self, request, view):
        usuario:UsuarioModel = request.user
        if usuario.tipoUsuario == 'MOZO':
            return True
        else:
            return False
        
class SoloTrabajador(BasePermission):
    message = 'Solamente los mozos o administradores puede realizar esta accion'

    def has_permission(self, request, view):
        usuario:UsuarioModel = request.user
        if usuario.tipoUsuario == 'MOZO' or usuario.tipoUsuario == 'ADMINISTRADOR':
            return True
        else:
            return False