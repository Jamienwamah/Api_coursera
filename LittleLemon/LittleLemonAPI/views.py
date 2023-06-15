from django.shortcuts import render

# Create your views here.
#The generic class has everything built into them for crud operations
from .models import MenuItems
from .serializers import MenuItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
#The list create view was extended from the generic module. The list create view, can accept record and display post calls to create new record
#To function correctly, the list create view needs the query set and the serializaer class
#The query set retrieves all the records using the module and a serializer to store all the retrieved methods
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        #Deserialization method
        items = MenuItems.objects.select_related('category').all()
        serializer_class = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    #To de-serialize the request data, you must pass in two serializers
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        # The request data must include all the essential field data
        serialized_item.is_valid(raise_exceptions=True)
        # Take note the data validator is built into serializer and it can be invoked using the is_valid method
        #To access the validated data, use the validated data property of serializer
        #serialized_item.validated_data
        #or we can use the save method to save the data
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

# class SingleMenuItemsView(generics.RetrieveUpdateAPIView):
#     queryset = MenuItems.objects.all()
#     serializer_class = MenuItemSerializer
#     #In the code snippet, the retrieve view update class has everything to fetch a record and uses the put method to update them
#     #While the destroy view class has everything to accept, delete calls and finally delete a record
 
@api_view()
def single_items(request):
    items = get_object_or_404(MenuItem, pk=id)
    serializer_class = MenuItemSerializer(item)
    return Response(serialized_item.data)
