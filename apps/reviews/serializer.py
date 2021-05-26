from . import models
from rest_framework import serializers


class ShopReviewSer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopReviewModel
        fields = '__all__'


class FollowupReviewSer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowupReviewModel
        fields = '__all__'


class OrderReviewSer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderReviewModel
        fields = '__all__'
