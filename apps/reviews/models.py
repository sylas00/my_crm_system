from django.db import models

from followups.models import FollowUpModel
from libs.soft_delete_model import BaseModel
from orders.models import OrderModel
from shops.models import ShopModel
from users.models import User


class ShopReviewModel(BaseModel):
    status = models.SmallIntegerField(choices=[(0, '待审核'), (2, '通过'), (3, '未通过')], default=0, verbose_name='审批状态')
    reason = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='原因')
    account = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="审批人")
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='review', verbose_name="关联店铺")

    class Meta:
        db_table = 'crm_shop_review'
        verbose_name = '新增店铺审批表'
        verbose_name_plural = verbose_name


class FollowupReviewModel(BaseModel):
    status = models.SmallIntegerField(choices=[(0, '待审核'), (2, '通过'), (3, '未通过')], default=0, verbose_name='审批状态')
    reason = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='原因')
    account = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="审批人")
    shop = models.ForeignKey(FollowUpModel, on_delete=models.CASCADE, related_name='review', verbose_name="关联跟进")

    class Meta:
        db_table = 'crm_followup_review'
        verbose_name = '新增跟进审批表'
        verbose_name_plural = verbose_name


class OrderReviewModel(BaseModel):
    status = models.SmallIntegerField(choices=[(0, '待审核'), (2, '通过'), (3, '未通过')], default=0, verbose_name='审批状态')
    reason = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='原因')
    account = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="审批人")
    shop = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='review', verbose_name="关联订单")

    class Meta:
        db_table = 'crm_order_review'
        verbose_name = '订单审批表'
        verbose_name_plural = verbose_name
