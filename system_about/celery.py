from time import sleep

import openpyxl
# from apps.users.models import User
from celery import Celery

import os
# 导入Django配置 导入配置要用 而且自动加载各个app的tasks也要用到
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_about.settings.dev')

app = Celery('handler')
app.autodiscover_tasks()

# 配置队列方案一：直接写在文件里
app.conf.broker_url = 'redis://127.0.0.1:6379/0'


# 配置队列方案二：当要从django的setting中导入配置时
# 载入settings中的celery配置
# app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task()
def out(x,y):
    print(x,y)
    data = [1]
    # data = User.objects.values_list('username', flat=True)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'data'
    ws['A1'] = 'name'
    sleep(10)
    for i in data:
        ws.append([i])
    wb.save('a.xlsx')
