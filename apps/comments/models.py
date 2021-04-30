from django.db import models
from followups.models import FollowUpModel
from libs.soft_delete_model import BaseModel
from shops.models import ShopModel
from users.models import User


class ShopCommentModel(BaseModel):
    reason = models.CharField(max_length=255, default='', verbose_name='评论')
    account = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="评论人")
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='comment', verbose_name="关联店铺")

    class Meta:
        db_table = 'crm_shop_comment'
        verbose_name = '店铺评论'
        verbose_name_plural = verbose_name


class FollowupCommentModel(BaseModel):
    reason = models.CharField(max_length=255, default='', verbose_name='评论')
    account = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="评论人")
    shop = models.ForeignKey(FollowUpModel, on_delete=models.CASCADE, related_name='comment', verbose_name="关联跟进记录")

    class Meta:
        db_table = 'crm_followup_comment'
        verbose_name = '跟进记录评论'
        verbose_name_plural = verbose_name
