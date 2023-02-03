from django.urls import path
from .views import CategoriaApiView

urlpatterns = [
    # cuando se acceda a la ruta /categorias/ se mandara a llamnar a la funcionaldiad de nuestra categoriaApiView
    path('categorias/', CategoriaApiView.as_view())
]