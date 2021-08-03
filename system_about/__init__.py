# 弃用了pymysql
# import pymysql
# pymysql.install_as_MySQLdb()

# 这将确保在 Django 启动时始终导入该应用程序，以便 shared_task 能使用该应用程序
# 注意 很关键 这个东西  当使用各app里的tasks的时候 需要这个配置 不然会出现请求一直等待相应的情况
from .celery import app as celery_app

__all__ = ('celery_app',)
