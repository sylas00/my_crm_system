from django.db import models

# Create your models here.
from customers.models import CustomerModel
from libs.soft_delete_model import BaseModel
from orders.models import OrderModel
from products.models import ProductTypeModel
from shops.models import ShopModel
from upload.models import ScreenshotModel, FollowUpDocumentModel, RecordingModel
from users.models import User


class SalesStageModel(BaseModel):
    """
    成功开场、业绩介绍、解答问题、约定付款 、成交
    """
    stage_name = models.CharField(max_length=255, verbose_name='销售阶段')

    class Meta:
        db_table = 'crm_sales_stage'
        verbose_name = '销售阶段表'
        verbose_name_plural = verbose_name


class FollowUpModel(BaseModel):
    """
    若需历史跟进记录则状态
    """
    # 跟进方式
    FOLLOWUP_WAY_CHOICES = [
        (0, '未知'),
        (1, '电话'),
        (2, '微信'),
        (3, 'QQ'),
        (4, '面谈'),
    ]
    # 绩效打标
    FOLLOWUP_MARK_CHOICES = [
        (0, '不打标'),
        (1, '新加意向'),
        (2, '回访意向'),
        (3, '合作转接'),
        (4, '特殊延伸'),
        (5, '客户跟踪'),
        (6, '成交'),
    ]
    # 意向程度
    INTENTIONAL = [
        (0, '未知'),
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
    ]
    # 销售状态
    SALE_STAGE_CHOICES = [
        (0, '未知'),
        (1, '成功开场'),
        (2, '业绩介绍'),
        (3, '解答问题'),
        (4, '约定付款'),
        (5, '成交'),
    ]
    founder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='跟进人')
    follow_way = models.SmallIntegerField(choices=FOLLOWUP_WAY_CHOICES, default=0, verbose_name='跟进方式')
    follow_time = models.DateTimeField(null=True, blank=True, verbose_name='跟进时间')
    follow_next_time = models.DateTimeField(null=True, blank=True, verbose_name='预计下次跟进时间')
    chat_record = models.TextField(default=None, null=True, blank=True, verbose_name='聊天记录')
    follow_description = models.CharField(max_length=255, blank=True, verbose_name='跟进情况描述')
    marking = models.SmallIntegerField(choices=FOLLOWUP_MARK_CHOICES, default=0, verbose_name='绩效打标')
    intentional = models.IntegerField(default=1, choices=INTENTIONAL, verbose_name='意向度')
    estimated_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='预估金额')
    estimated_date = models.DateField(null=True, blank=True, verbose_name='预估日期')
    sales_stage = models.SmallIntegerField(choices=SALE_STAGE_CHOICES, default=0, verbose_name='销售阶段')
    chat_screenshot = models.ManyToManyField(ScreenshotModel, blank=True, verbose_name='跟进聊天截图')
    chat_document = models.ManyToManyField(FollowUpDocumentModel, blank=True, verbose_name='跟进聊天文档')
    chat_recording = models.ManyToManyField(RecordingModel, blank=True, verbose_name='跟进聊天录音')
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='成交订单')
    shop = models.ForeignKey(ShopModel, on_delete=models.CASCADE, verbose_name='关联店铺')
    cooperative_business_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE, null=True, blank=True,
                                                  verbose_name='合作业务类型')

    class Meta:
        # ordering = ['follow_time', 'update_time']
        db_table = 'crm_followup'
        verbose_name = '跟进记录表'
        verbose_name_plural = verbose_name
