from django.shortcuts import render

# Create your views here.
#nastavujeme finalny view

#najprv mas model ako databazu, view to vykresluje a kontroler robi spravu pod tym (funkcie) a pod

from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
