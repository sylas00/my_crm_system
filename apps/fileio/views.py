from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from system_about.celery import out
from users.models import User


class FileOutput(APIView):
    def get(self, req):
        data =User.objects.values_list('username',flat=True)
        a = out.delay(data)
        return Response({
            'ok': 'a'
        })
