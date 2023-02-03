from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel
from .serializers import CAtegoriaSerializers
# List > Listar (get)
# Create > crear (post)

class CategoriaApiView(ListCreateAPIView):
    # al utilizar una vista generica que ya no es necesario definir el comportamiento para cuando sea get o post
    # queryset > es el comando que utilizara para llamar a la informacion de nuestra  bd
    
    # SELECT * FROM categoria
    queryset = CategoriaModel.objects.all()
    # serializer_class > se define una clase que se encaragra de convertir y transformar las informacion que viene desde el cliente y la informacion
    # que enviamos hacia el cliente en datos tangibles
    serializer_class = CAtegoriaSerializers

    # def get(self):
    #    pass

    # def post(self):
    #    pass