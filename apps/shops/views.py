from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from shops.models import ShopModel
from shops.serializer import ShopSer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = ShopModel.objects.all()
    serializer_class = ShopSer
