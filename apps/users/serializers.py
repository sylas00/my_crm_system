from .models import User
from rest_framework import serializers
from django.contrib.auth.models import Group,Permission


class UserSerializer(serializers.ModelSerializer):
    class Mate:
        model = User
        fields = '__all__'


class UserGroup(serializers.ModelSerializer):
    class Mate:
        model = Permission
        fields = '__all__'
