from softdelete.models import SoftDeleteObject
from django.db import models


class BaseModel(SoftDeleteObject, models.Model):
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        abstract = True
