from rest_framework import viewsets
from . import models
from . import serializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.PaymentModel.objects.all()
    serializer_class = serializer.PaymentSer
