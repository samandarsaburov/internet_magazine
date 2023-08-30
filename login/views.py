from django.shortcuts import render
from .models import CustomUser
from .serializer import CustomUserSerializer
from rest_framework import generics
# Create your views here.

class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer