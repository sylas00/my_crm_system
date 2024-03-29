from .models import User
from rest_framework import serializers
from django.contrib.auth.models import Group,Permission


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserGroup(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
