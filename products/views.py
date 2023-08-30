from django.shortcuts import render
from .models import ProductsModel
from .serializer import ProductSerializer
from rest_framework import generics
# Create your views here.

class Get_all(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer
    
class Create(generics.CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer
    
class Update(generics.UpdateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer
    
class Delete(generics.DestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer
