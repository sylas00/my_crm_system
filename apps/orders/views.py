from rest_framework import viewsets
from . import models
from . import serializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializer.OrderSer