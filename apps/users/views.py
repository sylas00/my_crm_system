from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
# 之前已经将apps加入了导包路径 如果再从apps开始导会报错
# RuntimeError: Model class apps.users.models.User doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
# from apps.users.models import User
from django.utils import timezone

from shops.models import ShopModel
from users.models import User


def index(r):
    if r.method == 'POST':
        # user = AvatarModel.objects.create()
        # file = r.FILES.get('fff', None)
        # user.file = file
        # user.save()
        user = User.objects.create()
        user.avatar = r.FILES.get('fff', None)
        user.save()
        return FileResponse(user.avatar)
    if r.method == 'GET':
        # obj = AvatarModel.objects.get(pk=9)
        # img = obj.file
        # return FileResponse(img)
        # s = ShopModel.objects.get(pk=4)
        # s.delete()
        # s.save()
        # import datetime
        # from django.utils.timezone import utc
        # utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)
        # print(utcnow)
        #
        a = timezone.now()
        # # b = timezone.datetime()
        # c = timezone.Local()
        # a = User.objects.first()
        # a = a.created_at
        # print(a)
        return HttpResponse(a,)
