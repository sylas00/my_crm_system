from rest_framework import viewsets
from . import models
from . import serializer


class ShopReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ShopReviewModel.objects.all()
    serializer_class = serializer.ShopReviewSer


class FollowupReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ShopReviewModel.objects.all()
    serializer_class = serializer.FollowupReviewSer


class OrderReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ShopReviewModel.objects.all()
    serializer_class = serializer.OrderReviewSer
