from django.urls import path
from .import views
#Create Urls Here

urlpatterns = [
    path('', views.MenuItemsView.as_view()),
]