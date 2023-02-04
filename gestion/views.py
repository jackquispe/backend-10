from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CAtegoriaSerializers, PlatoSerializer, CAtegoriaConPlatosSerializer
from rest_framework.response import Response
from rest_framework.request import Request
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

class PlatoApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def get(self, request: Request):
        # al colocar ':' indicamos que el tipo de dato sera esa variable
        # request > toda la inforamcion que viene del cliente
        # DOCUMENTACION DJANGO********
        # https://docs.djangoproject.com/en/4.1/topics/db/queries/
        
        
        # SELECT * FROM platos where disponibilidad = true
        resultado = PlatoModel.objects.filter(disponibilidad=True).all()

        print(resultado)
        # Aca llammaos al serializer y le pasamos la informacion proveniente de la bd
        # y cin el paramemtro many truee indicamos que le stamos pasando el arreglo de instancias
        serializador = PlatoSerializer(instance=resultado, many=True)
        print(serializador.data)
        return Response(data={
            'content': serializador.data
        })
    
    def post(self, request: Request):
        body = request.data
        # cuadno queremos verificar si la informacion entrante es valida entonces utiilizamos el parametro data envez del parametro instacnce
        serializador = PlatoSerializer(data=body)
        # es el encargado de validar si la data es correctra y cumple con todos los requisitos
        valida = serializador.is_valid()

        #if valida == False:
         
        #   return Response(data={
        #      'message': 'la informacion es invalida',
        #     # error > mostrar los errores solamente cuando la data no sea vlida
        #    'content': serializador.errors
        #})
        
        # si la data pasada al serializadpor es una data valid enonces esta info se guqardara en el atributo validated_data que es un diccionario
        # el validated_Data solo estar disponinble cuando mandemos ala validacion
        platoExistente = PlatoModel.objects.filter(nombre = body.get('nombre')).first()
        
        if platoExistente:
            return Response(data={
                'message': 'el plato con nombre {} ya existe'.format(platoExistente.nombre)
                
            })
        
        if valida==False:
            return Response(data={
                'message': 'la informacion es invalida',
                # error > mostrar los errores solamentte cuando al data sea valida
                'content': serializador.errors

            })
        

        # ASi guardamos la informacion en al base de datos utilizando el serializador
        nuevoPlato = serializador.save()
        print(nuevoPlato)
        serializar = PlatoSerializer(instance=nuevoPlato)
        return Response(data={
            'message': 'Plato creado exitosamemnte',
            # data > es la informacion convertida a un diccionario para que pueda ser entendida por el cliente
            'content': serializar.data
        })

class PlatoDestroyApiView(DestroyAPIView):
    # queryset = PlatoModel.objects.all()
    # serializer_class = PlatoSerializer

    def delete(self, request: Request, pk: int):
        print(pk)
        platoEncontrado = PlatoModel.objects.filter(id = pk, disponibilidad = True).first()

        if platoEncontrado is None:
            return Response(data={
                'message': 'El plato no existe'
            })
        
        # Le cambiamos la disponiblidad
        platoEncontrado.disponibilidad = False
        # guardamos los cambios en la bd
        platoEncontrado.save()

        return Response(data={
            'message': 'plato eliminado exitosamente'
        })
    

class ListarCAtegoriaApiView(ListAPIView):
    def get(self, request: Request, pk : int):
        categoriaEncontrada = CategoriaModel.objects.filter(id = pk).first()
        print(categoriaEncontrada)
        if categoriaEncontrada is None:
            return Response(data={
                'message': 'categoria no existe'
            })
        
        serializador = CAtegoriaConPlatosSerializer(instance=categoriaEncontrada)

        return Response(data={
            'content': serializador.data
        })