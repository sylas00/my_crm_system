# 弃用了pymysql
# import pymysql
# pymysql.install_as_MySQLdb()

# 这里是为了让其他包能方便地导入我们创建的celery app
from .celery import app as celery_app

__all__ = ('celery_app',)
