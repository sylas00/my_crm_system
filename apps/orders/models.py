from django.db import models
from django_minio_backend import MinioBackend

from customers.models import CustomerModel
from libs.soft_delete_model import BaseModel
from payment.models import PaymentModel
from products.models import ProductModel, GiveawayModel
from shops.models import ShopModel
from upload.models import OrderImageModel, OrderDocumentModel
from users.models import User


class OrderModel(BaseModel):
    TRANSACTION_TYPE_CHOICES = (
        (1, '新签'),
        (2, '续签'),
        (3, '增值')
    )

    COOPERATION_CYCLE_CHOICES = (
        (1, '单月'),
        (2, '三个月'),
        (3, '季度'),
        (4, '半年'),
        (5, '年度')
    )
    founder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, verbose_name='关联店铺')
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES, verbose_name='交易类型')
    customer = models.ManyToManyField(CustomerModel, verbose_name='关联联系人')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='关联服务产品')
    order_num = models.CharField(max_length=255, verbose_name='订单编号')
    settlement_order_num = models.CharField(max_length=255, blank=True, verbose_name='结算订单编号')
    invoice_num = models.CharField(max_length=255, blank=True, verbose_name='发票号码')
    invoice_top_num = models.CharField(max_length=255, blank=True, verbose_name='发票抬头')
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='实际金额')
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='服务开始时间')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='服务结束时间')
    order_pic = models.ForeignKey(OrderImageModel, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='订单付款截图')
    order_contract = models.ForeignKey(OrderDocumentModel, on_delete=models.CASCADE, null=True, blank=True,
                                       verbose_name='订单合同扫描件')
    giveaway = models.ManyToManyField(GiveawayModel, blank=True, verbose_name='赠品')
    payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, blank=True, verbose_name='支付方式')
    des_effect = models.TextField(blank=True, verbose_name='效果说明')
    cooperation_cycle = models.IntegerField(choices=COOPERATION_CYCLE_CHOICES, null=True, blank=True,
                                            verbose_name='合作周期')

    class Meta:
        db_table = 'crm_order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name
