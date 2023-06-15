from django.contrib import admin
from .models import MenuItems
from .models import Category

# Register your models here.
admin.site.register(MenuItems)
admin.site.register(Category)