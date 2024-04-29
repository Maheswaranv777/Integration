from django.shortcuts import render
from .models import mars
from .serializers import marsSerializer
from rest_framework import viewsets

class marsview(viewsets.ModelViewSet):
    queryset=mars.objects.all()
    serializer_class=marsSerializer

# Create your views here.
