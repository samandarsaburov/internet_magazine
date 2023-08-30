from django.shortcuts import render
from .models import OrderModel
from .serializer import OrderSerializer
from rest_framework import generics

# Create your views here.
# get all
class GetAll(generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    
    
# create
class Create(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    

# Update
class Update(generics.UpdateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    
# Delete   
class Delete(generics.DestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
