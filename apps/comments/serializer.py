from . import models
from rest_framework import serializers


class FollowupCommentSer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowupCommentModel
        fields = '__all__'


class ShopCommentSer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopCommentModel
        fields = '__all__'
