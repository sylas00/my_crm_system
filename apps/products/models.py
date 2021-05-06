from django.db import models
from django_minio_backend import MinioBackend

from libs.soft_delete_model import BaseModel


class GiveawayModel(BaseModel):
    name = models.CharField(max_length=255, blank=False, verbose_name='赠品名')

    class Meta:
        db_table = 'crm_product_giveaway'
        verbose_name = '产品赠品'
        verbose_name_plural = verbose_name


class ServiceTimeModel(BaseModel):
    service_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='价格')
    service_minimum_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='最低价格')
    service_times = models.IntegerField(null=True, blank=True, verbose_name='数量')

    class Meta:
        db_table = 'crm_product_service_time'
        verbose_name = '服务次数套餐'
        verbose_name_plural = verbose_name


class ProductTypeModel(BaseModel):
    name = models.CharField(max_length=255, blank=False, verbose_name='产品类型')

    class Meta:
        db_table = 'crm_product_type'
        verbose_name = '产品类型'
        verbose_name_plural = verbose_name


class ProductPlatformModel(BaseModel):
    name = models.CharField(max_length=255, blank=False, verbose_name='产品平台')

    class Meta:
        db_table = 'crm_product_platform'
        verbose_name = '产品平台'
        verbose_name_plural = verbose_name


class ProductModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='服务名称')
    platform = models.ForeignKey(ProductPlatformModel, related_name='product', on_delete=models.CASCADE, blank=True,
                                 verbose_name='产品平台')
    type = models.ForeignKey(ProductTypeModel, related_name='product', on_delete=models.CASCADE, verbose_name='产品类型')
    giveaway = models.ManyToManyField(GiveawayModel, related_name='product', blank=True, verbose_name='赠品')
    package_img = models.ImageField(upload_to="product/%Y/%m/%d", storage=MinioBackend(bucket_name='image'), blank=True,
                                    verbose_name='报价图片')
    contract_file = models.FileField(upload_to="product/%Y/%m/%d", storage=MinioBackend(bucket_name='doc'),
                                     blank=True, verbose_name='合同附件')
    # 收费模式
    charging_type = models.IntegerField(choices=((1, '服务周期'), (2, '服务次数')), default=1, verbose_name='收费模式')
    # 收费模式1 服务周期
    unified_price_year = models.DecimalField(max_digits=20, decimal_places=2,verbose_name='年度统一报价')
    minimum_price_year = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                             verbose_name='最低年度报价')
    unified_price_half_year = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                                  verbose_name='半年统一报价')
    minimum_price_half_year = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                                  verbose_name='最低半年报价')
    unified_price_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                                verbose_name='季度统一报价')
    minimum_price_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                                verbose_name='最低季度报价')
    unified_price_month = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                              verbose_name='月度统一报价')
    minimum_price_month = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                              verbose_name='最低月度报价')
    # 收费模式2 服务次数
    service_time = models.ManyToManyField(ServiceTimeModel, related_name='product', blank=True, verbose_name='服务次数套餐')
    hide = models.BooleanField(default=False, verbose_name='是否隐藏')

    class Meta:
        db_table = 'crm_product_product'
        verbose_name = '产品'
        verbose_name_plural = verbose_name
