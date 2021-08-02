from django.shortcuts import render
import openpyxl
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


class FileOutput(APIView):
    def get(self, req):
        data = User.objects.values_list('username',flat=True)
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title='data'
        ws['A1']='name'
        for i in data:
            ws.append([i])
        wb.save('a.xlsx')
        return Response({
            'ok':'ok'
        })
