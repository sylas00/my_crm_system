from time import sleep
import openpyxl
from celery import shared_task
from users.models import User


# 如果是定义在app里的任务 用shard_task装饰器
@shared_task(name='aaa')
def out(x,y):
    print(x,y)
    data = User.objects.values_list('username', flat=True)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'data'
    ws['A1'] = 'name'
    sleep(3)
    for i in data:
        ws.append([i])
    wb.save('a.xlsx')
    return 0

