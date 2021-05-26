from . import models
from rest_framework import serializers


class GiveawaySer(serializers.ModelSerializer):
    class Meta:
        model = models.GiveawayModel
        fields = '__all__'


class ServiceTimeSer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceTimeModel
        fields = '__all__'


class ProductTypeSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductTypeModel
        fields = '__all__'


class ProductPlatformSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductPlatformModel
        fields = '__all__'


class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'
