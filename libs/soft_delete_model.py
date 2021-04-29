import datetime

from django.db import models


class BaseModel(models.Model):
    createdAt = models.DateTimeField("创建时间", auto_now_add=True)
    updatedAt = models.DateTimeField("更新时间", auto_now=True)
    deletedAt = models.DateTimeField("删除时间", null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.deletedAt = datetime.datetime.now()
        self.save()

    class Meta:
        abstract = True
