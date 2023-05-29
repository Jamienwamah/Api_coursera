from django.urls import path
from . import views
 #Create urls 
 
urlpatterns = [
     path('',views.books),
 ]