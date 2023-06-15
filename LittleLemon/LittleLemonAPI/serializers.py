from rest_framework import serializers
from .models import MenuItems
from .models import Category
from decimal import Decimal
#Create serializers here

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
#Lets change the name of a field using seializers
    stock = serializers.IntegerField(source = 'inventory')
   #linking the  calculate tax method as a new field in serializer
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    
    class Meta:
        model = MenuItems
        #fields = '__all__'
        fields = ['title', 'price', 'stock', 'price_after_tax', 'category']
        
    #Introducing a new field in serializer
    def calculate_tax(self, product:MenuItems):
        return product.price * Decimal(1.1)
    