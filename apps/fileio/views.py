from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import out
from users.models import User


class FileOutput(APIView):
    def get(self, req):
        data = User.objects.values_list('username', flat=True)
        # 用delay调用方法 如果不用delay就和调用原函数没区别 没有异步
        a = out.delay(1, 2)
        print(a.id)
        print(a.task_id)
        return Response({
            'ok': 'a'
        })
