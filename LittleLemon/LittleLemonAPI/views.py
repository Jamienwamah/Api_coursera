from django.shortcuts import render
from .serializers import MenuItemSerializer
from rest_framework import generics
from .models import MenuItems
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer