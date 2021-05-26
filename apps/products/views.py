from rest_framework import viewsets
from . import models
from . import serializer


class GiveawayViewSet(viewsets.ModelViewSet):
    queryset = models.GiveawayModel.objects.all()
    serializer_class = serializer.GiveawaySer


class ServiceTimeViewSet(viewsets.ModelViewSet):
    queryset = models.ServiceTimeModel.objects.all()
    serializer_class = serializer.ServiceTimeSer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ProductTypeModel.objects.all()
    serializer_class = serializer.ProductTypeSer


class ProductPlatformViewSet(viewsets.ModelViewSet):
    queryset = models.ProductPlatformModel.objects.all()
    serializer_class = serializer.ProductPlatformSer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializer.ProductSer
