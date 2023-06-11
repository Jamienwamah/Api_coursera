#The generic class has everything built into them for crud operations
from django.shortcuts import render
from .serializers import MenuItemSerializer
from rest_framework import generics
from .models import MenuItems
# Create your views here.
#The list create view was extended from the generic module. The list create view, can accept record and display post calls to create new record
#To function correctly, the list create view needs the query set and the serializaer class
#The query set retrieves all the records using the module and a serializer to store all the retrieved methods
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer