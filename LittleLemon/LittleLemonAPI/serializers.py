from rest_framework import serializers
from .models import MenuItems
#Create serializers here

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'
    