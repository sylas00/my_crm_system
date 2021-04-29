from django.db import models




from libs.soft_delete_model import BaseModel
from users.models import User



class PlatformModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='客户平台')

    class Meta:
        db_table = 'crm_shop_platform'
        verbose_name = '客户平台'
        verbose_name_plural = verbose_name


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='类目名称')
    platform = models.ForeignKey(PlatformModel, on_delete=models.CASCADE, related_name='categories', null=True, blank=True, verbose_name='客户平台')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True, verbose_name='上级类别')

    class Meta:
        db_table = 'crm_shop_store_category'
        verbose_name = '店铺类目表'
        verbose_name_plural = verbose_name


class StoreLevelModel(models.Model):
    platform = models.ForeignKey(PlatformModel, on_delete=models.CASCADE, related_name='StoreLevel', null=True, blank=True, verbose_name='客户平台')
    name = models.CharField(max_length=255, verbose_name='店铺层级')

    class Meta:
        db_table = 'crm_shop_store_level'
        verbose_name = '店铺层级'
        verbose_name_plural = verbose_name


class StoreTypeModel(models.Model):
    platform = models.ForeignKey(PlatformModel, on_delete=models.CASCADE, related_name='StoreType', null=True, blank=True, verbose_name='客户平台')
    name = models.CharField(max_length=255, verbose_name='店铺类型')

    class Meta:
        db_table = 'crm_shop_store_type'
        verbose_name = '店铺类型'
        verbose_name_plural = verbose_name


class TransactionCycleModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='成交周期')

    class Meta:
        db_table = 'crm_shop_transaction_cycle'
        verbose_name = '成交周期'
        verbose_name_plural = verbose_name


class ShopNatureModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='店铺性质')

    class Meta:
        db_table = 'crm_shop_shop_nature'
        verbose_name = '店铺性质'
        verbose_name_plural = verbose_name


class SupplySituationModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='货源情况')

    class Meta:
        db_table = 'crm_shop_supply_situation'
        verbose_name = '货源情况'
        verbose_name_plural = verbose_name


class MainFollowupMethodsModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='主要跟进方式')

    class Meta:
        db_table = 'crm_shop_main_followup_method'
        verbose_name = '主要跟进方式'
        verbose_name_plural = verbose_name


class OpeningTimeModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='开店时长')

    class Meta:
        db_table = 'crm_shop_opening_time'
        verbose_name = '开店时长'
        verbose_name_plural = verbose_name


class ShopModel(BaseModel):
    shop_name = models.CharField(max_length=255, unique=True, verbose_name='店铺名')
    url = models.CharField(max_length=1024, default='', null=True, blank=True, verbose_name='店铺链接')
    credit_rating = models.CharField(max_length=255, null=True, blank=True, verbose_name='信用等级')
    product_quantity = models.IntegerField(null=True, blank=True, verbose_name='产品数量')
    cumulative_sales = models.IntegerField(null=True, blank=True, verbose_name='累计销售量')
    sales = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name='销售额')
    shop_opening_time = models.DateField(null=True, blank=True, verbose_name='开店时间')
    create_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='创建人')
    # review = models.ForeignKey(ShopReviewModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='新增店铺审批')
    opening_time = models.ForeignKey(OpeningTimeModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='开店周期')
    main_followup_method = models.ForeignKey(MainFollowupMethodsModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='主要跟进方式')
    supply_situation = models.ForeignKey(SupplySituationModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='货源情况')
    shop_nature = models.ForeignKey(ShopNatureModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='店铺性质')
    transaction_cycle = models.ForeignKey(TransactionCycleModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='成交周期')
    platform = models.ForeignKey(PlatformModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='店铺平台')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='店铺类目')
    store_level = models.ForeignKey(StoreLevelModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='店铺层级')
    store_type = models.ForeignKey(StoreTypeModel, on_delete=models.CASCADE, related_name='shops', null=True, blank=True, verbose_name='店铺类型')

    class Meta:
        db_table = 'crm_shop'
        verbose_name = '客户店铺信息表'
        verbose_name_plural = verbose_name
