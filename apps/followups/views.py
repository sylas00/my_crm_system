from . import models
from . import serializer
from rest_framework import viewsets


class FollowUpViewSet(viewsets.ModelViewSet):
    queryset = models.FollowUpModel.objects.all()
    serializer_class = serializer.FollowUpSer
