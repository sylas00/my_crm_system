from django.db import models

from customers.models import CustomerModel
from libs.soft_delete_model import BaseModel
from shops.models import ShopModel
from users.models import User


class OrderModel(BaseModel):
    TRANSACTION_TYPE_CHOICES = (
        (1, '新签'),
        (2, '续签'),
        (3, '增值')
    )

    COOPERATION_CYCYLE_CHOICES = (
        (1, '单月'),
        (2, '三个月'),
        (3, '季度'),
        (4, '半年'),
        (5, '年度')
    )

    HELP_LEVEL_CHOICES = (
        (1, '2%'),
        (2, '10%'),
        (3, '30%'),
        (4, '50%')
    )

    COMMISSION_CHOICE = (
        (1, '1%'),
        (2, '2%'),
        (3, '2.5%'),
        (4, '3%'),
        (5, '3.5%'),
        (6, '4%'),
        (7, '4.5%'),
        (8, '5%'),
        (9, '5.5%'),
        (10, '6%'),
        (11, '7%'),
        (12, '8%'),
        (13, '9%'),
        (14, '10%'),
    )
    founder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order', null=True, blank=True,
                                verbose_name='创建人')
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='order', verbose_name='关联店铺')
    customer = models.ManyToManyField(CustomerModel, related_name='order', null=True, blank=True, verbose_name='关联联系人')
    # product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='order', null=True, blank=True,
    #                             verbose_name='关联服务产品')
    order_num = models.CharField(max_length=255, null=True, blank=True, verbose_name='订单编号')
    settlement_order_num = models.CharField(max_length=255, null=True, blank=True, verbose_name='结算订单编号')
    invoice_num = models.CharField(max_length=255, null=True, blank=True, verbose_name='发票号码')
    invoice_top_num = models.CharField(max_length=255, null=True, blank=True, verbose_name='发票抬头')
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='实际金额')
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='服务开始时间')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='服务结束时间')
    # order_pic = models.ManyToManyField(OrderPicModel, related_name='order', blank=True, verbose_name='订单付款截图')
    # order_contract = models.ManyToManyField(OrderContractFileModel, related_name='order', blank=True,
    #                                         verbose_name='订单合同扫描件')
    attach = models.TextField(max_length=255, null=True, blank=True, verbose_name='附加赠品')
    # payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, related_name='order', null=True, blank=True,
    #                             verbose_name='支付方式')
    effect = models.BooleanField(null=True, blank=True, default=True, verbose_name='是否保证效果')
    whether_to_cooperate = models.BooleanField(null=True, blank=True, default=True, verbose_name='是否合作转接')
    whether_to_cooperate_person = models.ForeignKey(User, on_delete=models.CASCADE,
                                                    related_name='whether_to_cooperate_person', null=True, blank=True,
                                                    verbose_name='合作转接人')
    des_effect = models.TextField(null=True, blank=True, verbose_name='效果说明')
    effect_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='保证金额')
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES, null=True, blank=True, verbose_name='交易类型')
    commission = models.BooleanField(default=False, null=True, blank=True, verbose_name='是否有提成')
    commission_start = models.IntegerField(choices=COMMISSION_CHOICE, null=True, blank=True, verbose_name='提点比例开始')
    commission_end = models.IntegerField(choices=COMMISSION_CHOICE, null=True, blank=True, verbose_name='提点比例结束')
    mention = models.TextField(null=True, blank=True, verbose_name='提点说明')
    is_help = models.BooleanField(default=False, verbose_name='是否帮谈')
    helper = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_helper', null=True,
                               blank=True, verbose_name='帮谈人')
    help_level = models.IntegerField(choices=HELP_LEVEL_CHOICES, verbose_name='帮谈提点')
    cooperation_cycle = models.IntegerField(choices=COOPERATION_CYCYLE_CHOICES, verbose_name='合作周期')

    class Meta:
        # ordering = ['-update_time', '-create_time']
        db_table = 'crm_order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name
