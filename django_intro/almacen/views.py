from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel
from .serializers import ProductosSerializer
from rest_framework import generics

# Create your views here.

def renderHtml(request):
    return HttpResponse("<button>hola</button>")

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first()
    return HttpResponse(f'El producto encontrado se llama {producto.nombre} y el precio {producto.precio}')

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer
