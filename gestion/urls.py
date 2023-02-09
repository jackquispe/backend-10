from django.urls import path
from .views import CategoriaApiView, PlatoApiView, PlatoDestroyApiView, ListarCAtegoriaApiView, RegistroUsuarioApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # cuando se acceda a la ruta /categorias/ se mandara a llamnar a la funcionaldiad de nuestra categoriaApiView
    path('categorias/', CategoriaApiView.as_view()),
    path('platos/', PlatoApiView.as_view()),
    path('plato/<int:pk>', PlatoDestroyApiView.as_view()),
    path('categoria/<int:pk>', ListarCAtegoriaApiView.as_view()),
    path('registro/', RegistroUsuarioApiView.as_view()),
    path('login/', TokenObtainPairView.as_view())
    
]