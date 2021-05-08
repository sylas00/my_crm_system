from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Mate:
        model = User
        # fields=
