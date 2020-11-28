from django.shortcuts import render
from rest_framework import generics,filters

# Create your views here.
from todos import models
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = TodoSerializer

class TodoAPIView(generics.ListCreateAPIView):
    search_fields = ['categoria', 'descripcion']
    filter_backends = (filters.SearchFilter, )
    queryset = models.Categoria.objects.all()
    serializer_class = TodoSerializer