from django.urls import path
from . import views

urlpatterns = [
    # path('menu-items', views.MenuItemsView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemsView.as_view()),
    path('menu_items', views.menu_items),
    path('single_items', views.single_items),
]
