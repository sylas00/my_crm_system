from time import sleep
from celery import Celery
import os

# 启动任务命令：
# celery -A system_about worker -l INFO
# 注意是在manege.py的同级目录下  也就是 celery文件所在 包 的存在路径下


# 导入Django配置 导入配置要用 而且自动加载各个app的tasks也要用到
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_about.settings.dev')

# 配置方法一：直接在创建celery实例的时候指定
# 定义celery实例的时候名称可以任意
app = Celery('a', broker='redis://127.0.0.1:6379/0',backend='redis://localhost:6379/1')

# 配置队列方案二：直接写在文件里
# app.conf.broker_url = 'redis://127.0.0.1:6379/0'
# 配置任务状态和任务结果后端
# app.conf.result_backend = 'redis://localhost:6379/1'


# 配置队列方案三：当要从django的setting中导入配置时
# 载入settings中的celery配置 必须以CELERY_开头
# app.config_from_object('django.conf:settings', namespace='CELERY')

# 配置方案四：从某个文件载入配置
# app.config_from_object('celeryconfig')

#从在setting注册的APP中自动载入所有任务
app.autodiscover_tasks()


@app.task(name='wuhu') #这里task加不加括号都可  可与用name指定名字
def out():
    # print(data)
    # # data = [1]
    # wb = openpyxl.Workbook()
    # ws = wb.active
    # ws.title = 'data'
    # ws['A1'] = 'name'
    # sleep(10)
    # for i in data:
    #     ws.append([i])
    # wb.save('a.xlsx')
    sleep(10)
    return 0
