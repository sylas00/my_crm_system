from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render

# Create your views here.
# 之前已经将apps加入了导包路径 如果再从apps开始导会报错
# RuntimeError: Model class apps.users.models.User doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
# from apps.users.models import User

from users.models import AvatarModel


def index(r):
    if r.method == 'POST':
        user = AvatarModel.objects.create()
        file = r.FILES.get('fff', None)
        user.file = file
        user.save()
        return HttpResponse('hello world')
    if r.method == 'GET':
        obj = AvatarModel.objects.get(pk=9)
        img = obj.file
        return FileResponse(img)

