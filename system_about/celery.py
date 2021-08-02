from celery import Celery
import os



app = Celery('handler')

# 配置方案一：直接写在文件里
app.conf.broker_url = 'redis://127.0.0.1:6379/0'

# 配置方案二：当要从django的setting中导入配置时
# 导入Django配置
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_about.settings.dev')
# 载入settings中的celery配置
# app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def add(x, y):
    return x + y
