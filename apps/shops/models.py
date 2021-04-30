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


class CustomerSourceModel(BaseModel):
    """
    独立开发、公海赎回、同事转接、指定分配
    """
    source_name = models.CharField(max_length=255, verbose_name='客户来源')

    class Meta:
        db_table = 'crm_customer_source'
        verbose_name = '客户来源表'
        verbose_name_plural = verbose_name


class ShopModel(BaseModel):
    REVIEW_CHOICES = [
        (0, '待审核'),
        (1, '通过'),
        (2, '未通过'),
    ]
    FOLLOWUP_METHOD_CHOICES = [
        (0, '未知'),
        (1, '电话沟通'),
        (2, '网络沟通'),
        (3, '面谈'),
    ]
    PLATFORM_CHOICES = [
        (0, '未知'),
        (1, '淘宝'),
        (2, '天猫'),
        (3, '京东'),
        (4, '拼多多'),

    ]
    name = models.CharField(max_length=255, unique=True, verbose_name='店铺名')
    url = models.URLField(max_length=1024, default='', blank=True, verbose_name='店铺链接')
    product_quantity = models.IntegerField(null=True, blank=True, verbose_name='产品数量')
    cumulative_sales = models.IntegerField(null=True, blank=True, verbose_name='累计销售量')
    sales = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='销售额')
    shop_opening_time = models.DateField(null=True, blank=True, verbose_name='开店时间')
    create_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops', null=True, blank=True,
                                      verbose_name='创建人')
    shop_own = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_own', null=True, blank=True,
                                 verbose_name='负责人')
    # review = models.ForeignKey(ShopReviewModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='新增店铺审批')
    main_followup_method = models.SmallIntegerField(choices=FOLLOWUP_METHOD_CHOICES, default=0, verbose_name='主要跟进方式')
    platform = models.SmallIntegerField(choices=PLATFORM_CHOICES,default=0, verbose_name='店铺平台')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True,
                                 verbose_name='店铺类目')
    is_close = models.BooleanField(null=True, blank=True, default=False, verbose_name='是否关店')
    locked = models.BooleanField(null=True, blank=True, default=False, verbose_name='锁定客户')
    lock_time = models.DateTimeField(null=True, blank=True, verbose_name='锁定时间')
    add_partner_time = models.DateTimeField(null=True, blank=True, verbose_name='添加合作人时间')
    partner = models.ManyToManyField(User, related_name='customer_partner', blank=True, verbose_name='合作人')
    customer_source = models.ForeignKey(CustomerSourceModel, on_delete=models.CASCADE, related_name='customer',
                                        null=True, blank=True, verbose_name='店铺来源')
    review = models.IntegerField(choices=REVIEW_CHOICES, default=0, verbose_name='审核状态')

    class Meta:
        db_table = 'crm_shop'
        verbose_name = '客户店铺信息表'
        verbose_name_plural = verbose_name
