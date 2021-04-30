from django.db import models

# Create your models here.
from customers.models import CustomerModel
from libs.soft_delete_model import BaseModel
from users.models import User


class FollowWaysModel(BaseModel):
    """
    电话、微信、QQ、面谈
    """
    way_name = models.CharField(max_length=255, verbose_name='跟进方式')

    class Meta:
        db_table = 'crm_follow_ways'
        verbose_name = '跟进方式表'
        verbose_name_plural = verbose_name


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

    follow_account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followup', verbose_name='跟进人')
    follow_way = models.ForeignKey(FollowWaysModel, on_delete=models.CASCADE, related_name='followup', null=True,
                                   blank=True, verbose_name='跟进方式')
    follow_time = models.DateTimeField(null=True, blank=True, verbose_name='跟进时间')
    follow_next_time = models.DateTimeField(null=True, blank=True, verbose_name='下次跟进时间')
    chat_record = models.TextField(default=None, null=True, blank=True, verbose_name='聊天记录')
    follow_description = models.CharField(max_length=255, null=True, blank=True, verbose_name='跟进情况描述')
    marking = models.IntegerField(default=1, null=False, blank=False,
                                  verbose_name='绩效打标')  # 1不打标  2新加意向  3回访意向 4合作转接 5特殊延伸 6成交 7客户跟踪
    intentional = models.IntegerField(default=1, choices=((1, 'D'), (2, 'C'), (3, 'B'), (4, 'A')), null=True,
                                      blank=True, verbose_name='意向度')
    estimated_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='预估金额')
    estimated_date = models.DateField(null=True, blank=True, verbose_name='预估日期')
    sales_stage = models.ForeignKey(SalesStageModel, on_delete=models.CASCADE, related_name='follows_sales_stage',
                                    null=True, blank=True, verbose_name='销售阶段')
    # chat_screenshot = models.ManyToManyField(ScreenshotModel, related_name='followup', blank=True, verbose_name='跟进聊天截图')
    # chat_document = models.ManyToManyField(DocumentModel, related_name='followup', blank=True, verbose_name='跟进聊天文档')
    # chat_recording = models.ManyToManyField(RecordingModel, related_name='followup', blank=True, verbose_name='跟进聊天录音')
    # comment = models.ManyToManyField(CommentModel, related_name='followup', blank=True, verbose_name='评论')
    # order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='followup', null=True, blank=True, verbose_name='成交订单')
    shop = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='followup', blank=True,
                                 verbose_name='关联联系人')

    # cooperative_business_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE, related_name='followup', null=True, blank=True, verbose_name='合作业务类型')

    class Meta:
        # ordering = ['follow_time', 'update_time']
        db_table = 'crm_followup'
        verbose_name = '跟进记录表'
        verbose_name_plural = verbose_name
