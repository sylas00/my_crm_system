from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse, FileResponse
# 之前已经将apps加入了导包路径 如果再从apps开始导会报错
# RuntimeError: Model class apps.users.models.User doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
from django.utils import timezone
from rest_framework import viewsets, permissions

from users.models import User
from users.serializers import UserGroup


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = UserGroup
    # permission_classes = [permissions.IsAuthenticated]

