from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse, FileResponse
# 之前已经将apps加入了导包路径 如果再从apps开始导会报错
# RuntimeError: Model class apps.users.models.User doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
from django.utils import timezone
from rest_framework import viewsets, permissions

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSer
    # permission_classes = [permissions.IsAuthenticated]
