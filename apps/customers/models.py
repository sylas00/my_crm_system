from django.db import models

from libs.soft_delete_model import BaseModel
from shops.models import ShopModel
from users.models import User


# 自关联的表 导入的时候 一级类目的parent如果是-1 这样的 会报错 因为找不到主键为-1的行 所以设置为允许null 直接把一级类目的parent设置成null
class AreaModel(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, verbose_name='名称')
    short_name = models.CharField(max_length=10, blank=True, null=True, verbose_name='简称')
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name='邮编')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='上一级行政区')
    level = models.IntegerField(blank=True, null=True, verbose_name='级别', )

    class Meta:
        db_table = 'crm_area'
        verbose_name = '行政区划'
        verbose_name_plural = verbose_name


class CustomerModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='客户名')
    founder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, verbose_name='客户所属店铺')
    qq = models.CharField(max_length=255, blank=True, verbose_name='QQ')
    wechat = models.CharField(max_length=255, blank=True, verbose_name='微信')
    phone = models.CharField(max_length=11, blank=True, verbose_name='手机号')
    tel = models.CharField(max_length=255, blank=True, verbose_name='座机电话')
    address = models.ForeignKey(AreaModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='地址')

    # 操作记录 投诉 举报

    class Meta:
        db_table = 'crm_customer'
        verbose_name = '客户表'
        verbose_name_plural = verbose_name
