from rest_framework import viewsets
from . import models
from . import serializer


class FollowupCommentViewSet(viewsets.ModelViewSet):
    queryset = models.FollowupCommentModel.objects.all()
    serializer_class = serializer.FollowupCommentSer


class ShopCommentViewSet(viewsets.ModelViewSet):
    queryset = models.FollowupCommentModel.objects.all()
    serializer_class = serializer.ShopCommentSer
