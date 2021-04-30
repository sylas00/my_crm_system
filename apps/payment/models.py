from django.db import models
# Create your models here.
from libs.soft_delete_model import BaseModel


class PaymentModel(BaseModel):
    channel = models.CharField(max_length=255, blank=True, null=True, verbose_name='付款渠道')
    name = models.TextField(blank=True, null=True, verbose_name='账户/名称')
    method = models.CharField(max_length=255, blank=True, null=True, verbose_name='支付方式')
    remark = models.TextField(blank=True, null=True, verbose_name='备注说明')
    hide = models.BooleanField(default=False, verbose_name='是否隐藏')

    class Meta:
        db_table = 'crm_payment'
        verbose_name = '付款方式'
        verbose_name_plural = verbose_name
