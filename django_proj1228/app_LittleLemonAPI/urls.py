from django.urls import path
from . import views


urlpatterns = [
    path('', views.home2),
    path('menu-items', views.MenuItemView.as_view()),
    path('notes', views.notes()),
]