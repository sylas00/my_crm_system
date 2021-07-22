from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse, FileResponse
# 之前已经将apps加入了导包路径 如果再从apps开始导会报错
# RuntimeError: Model class apps.users.models.User doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.decorators import cache_response

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSer
    # permission_classes = [permissions.IsAuthenticated]

# 测试缓存用的视图
class Useraaa(APIView):
    # 增加缓存 第一次查会连接数据库  后面直接用缓存 测试在django3.2 会报'Response' object has no attribute '_headers'的错
    # 切换成3.1就可以了 多看这些包的官方文档
    @cache_response(timeout=300,cache='default')
    def get(self, req):
        print(models.User.objects.all())
        return Response({'asd': 1})
