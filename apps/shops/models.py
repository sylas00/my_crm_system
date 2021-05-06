from django.db import models

from libs.soft_delete_model import BaseModel
from users.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='类目名称')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True,
                               verbose_name='上级类别')

    class Meta:
        db_table = 'crm_shop_store_category'
        verbose_name = '店铺类目表'
        verbose_name_plural = verbose_name


class ShopModel(BaseModel):
    # 主要跟进方式
    FOLLOWUP_METHOD_CHOICES = [
        (0, '未知'),
        (1, '电话沟通'),
        (2, '网络沟通'),
        (3, '面谈'),
    ]
    # 店铺平台
    PLATFORM_CHOICES = [
        (0, '未知'),
        (1, '淘宝'),
        (2, '天猫'),
        (3, '京东'),
        (4, '拼多多'),
        (5, '亚马逊'),
    ]
    # 客户来源
    SOURCE_CHOICES = [
        (0, '未知'),
        (1, '独立开发'),
        (2, '指定分配'),
        (3, '同事转接'),
    ]
    name = models.CharField(max_length=255, unique=True, verbose_name='店铺名')
    url = models.URLField(max_length=1024, blank=True, verbose_name='店铺链接')
    product_quantity = models.IntegerField(blank=True, null=True, verbose_name='产品数量')
    cumulative_sales = models.IntegerField(blank=True, null=True, verbose_name='累计销售量')
    sales = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='销售额')
    shop_opening_time = models.DateField(null=True, blank=True, verbose_name='开店时间')
    create_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops', verbose_name='创建人')
    locked = models.BooleanField(default=False, verbose_name='锁定客户')
    lock_time = models.DateTimeField(null=True, blank=True, verbose_name='锁定时间')
    add_partner_time = models.DateTimeField(null=True, blank=True, verbose_name='添加合作人时间')
    partner = models.ManyToManyField(User, related_name='customer_partner', blank=True, verbose_name='合作人')
    customer_source = models.SmallIntegerField(choices=SOURCE_CHOICES, default=0, verbose_name='店铺来源')
    followup_method = models.SmallIntegerField(choices=FOLLOWUP_METHOD_CHOICES, default=0, verbose_name='主要跟进方式')
    platform = models.SmallIntegerField(choices=PLATFORM_CHOICES, default=0, verbose_name='店铺平台')
    shop_own = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_own', null=True, blank=True,
                                 verbose_name='负责人')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True,
                                 verbose_name='店铺类目')
    is_close = models.BooleanField(default=False, verbose_name='是否关店')

    class Meta:
        db_table = 'crm_shop'
        verbose_name = '客户店铺信息表'
        verbose_name_plural = verbose_name
