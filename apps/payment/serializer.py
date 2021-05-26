from . import models
from rest_framework import serializers


class PaymentSer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentModel
        fields = '__all__'
