from . import models
from rest_framework import serializers


class FollowUpSer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowUpModel
        fields = '__all__'
