from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from system_about.celery import out


class FileOutput(APIView):
    def get(self, req):
        a = out.delay(1,2)
        return Response({
            'ok': 'a'
        })
