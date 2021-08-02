# 弃用了pymysql
# import pymysql
# pymysql.install_as_MySQLdb()


# 当Django 启动时加载应用程序，以便将各个app里被@shared_task装饰器装饰的函数导入celery处理
# from .celery import app as celery_app
#
# __all__ = ('celery_app',)