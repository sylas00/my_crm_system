from django.db import models

from libs.soft_delete_model import BaseModel
from shops.models import ShopModel
from users.models import User


class AreaModel(models.Model):
    """
    行政区划
    null = True：（必写项）允许省级的父级为空
    blank = True：（必写项）约束将来在admin站点
    parent表单里可以不填
    on_delete：删除守护，比如将来需要删除某个市，如果不做守护，会把这个市下面的区全都删掉
    """
    name = models.CharField(max_length=20, verbose_name='名称')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', blank=True,
                               verbose_name='上一级行政区')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_areas'
        verbose_name = '行政区划'
        verbose_name_plural = verbose_name


class CustomerModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='客户名')
    create_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_create',
                                       verbose_name='创建人')
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='customer', verbose_name='客户所属店铺')
    qq = models.CharField(max_length=255, blank=True, verbose_name='QQ')
    wechat = models.CharField(max_length=255, blank=True, verbose_name='微信')
    phone = models.CharField(max_length=11, blank=True, verbose_name='手机号')
    tel = models.CharField(max_length=255, blank=True, verbose_name='座机电话')
    address = models.ForeignKey(AreaModel, on_delete=models.CASCADE, related_name='contact', blank=True,
                                verbose_name='地址')

    # 操作记录 投诉 举报

    class Meta:
        db_table = 'crm_customer'
        verbose_name = '客户表'
        verbose_name_plural = verbose_name
