import datetime
from softdelete.models import SoftDeleteObject
from django.db import models


class BaseModel(SoftDeleteObject, models.Model):
    createdAt = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updatedAt = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        abstract = True
