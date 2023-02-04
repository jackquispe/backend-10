from rest_framework import serializers
from .models import CategoriaModel, PlatoModel

class CAtegoriaSerializers(serializers.ModelSerializer):
    # cuando utilizamos un serializador basandonos enn un modelo se declara las clase meta
    class Meta:
        # este se encaragra de mapear todos los atributos del modelo para hacer
        # concordar el tipo de dato y sus especificaciones
        model = CategoriaModel
        # fields > sirve para indicar que columnas de la tabla queremos trabajar __all__
        # caso cointrario podremos manjera con los nombres de las columnas
        fields = '__all__'
        # si queremos excluir utilizaremos exclude
        # exclude = ['id']
        # NOTA: no se puede trabajar con el exclude y el fields a la vez.

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad']
        # este qatributo sirve para poder conectarnos a las relaciones adyacentes a este modelo
        # el depth sirve para decir que desde la tabla platos podamos mnovernos un nivel mas y devolver su categoria
        depth = 1

class CAtegoriaConPlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'
        

