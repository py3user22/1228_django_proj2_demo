from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import render


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

def home2(request):
    return render(request, '1229_django_serializers_install.html', {})

def single_item(request):
    return render(request, '1230_menu_item.html', {})

def notes(request):
    return render(request, '1231_django_notes.html', {})



