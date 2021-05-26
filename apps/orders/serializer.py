from . import models
from rest_framework import serializers


class OrderSer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderModel
        fields = '__all__'
