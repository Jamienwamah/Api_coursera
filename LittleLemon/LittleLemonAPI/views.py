from django.shortcuts import render

# Create your views here.
#The generic class has everything built into them for crud operations
from .models import MenuItems
from .serializers import MenuItemSerializer
from rest_framework import generics
# Create your views here.
#The list create view was extended from the generic module. The list create view, can accept record and display post calls to create new record
#To function correctly, the list create view needs the query set and the serializaer class
#The query set retrieves all the records using the module and a serializer to store all the retrieved methods
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    #In the code snippet, the retrieve view update class has everything to fetch a record and uses the put method to update them
    #While the destroy view class has everything to accept, delete calls and finally delete a record
 