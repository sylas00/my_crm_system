from django.db import models

from django_minio_backend import MinioBackend

from libs.soft_delete_model import BaseModel


# 文件表与主体表分离 好处 可以存更多关于文件的信息 坏处 麻烦


class AvatarModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.ImageField(upload_to="avatar/%Y/%m/%d", storage=MinioBackend(bucket_name='image'),
                             verbose_name='头像图片文件')

    class Meta:
        db_table = 'upload_avatar_image'
        verbose_name = '用户头像'
        verbose_name_plural = verbose_name


class ScreenshotModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.ImageField(upload_to="followup/%Y/%m/%d", storage=MinioBackend(bucket_name='image'),
                             verbose_name='跟进聊天截图')

    class Meta:
        db_table = 'upload_followup_image'
        verbose_name = '跟进聊天截图'
        verbose_name_plural = verbose_name


class OrderImageModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.ImageField(upload_to="order/%Y/%m/%d", storage=MinioBackend(bucket_name='image'),
                             verbose_name='订单付款截图')

    class Meta:
        db_table = 'upload_order_image'
        verbose_name = '跟进聊天截图'
        verbose_name_plural = verbose_name


class FollowUpDocumentModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.FileField(upload_to="followup/%Y/%m/%d", storage=MinioBackend(bucket_name='doc'),
                            verbose_name='跟进聊天文档')

    class Meta:
        db_table = 'upload_followup_document'
        verbose_name = '跟进聊天文档'
        verbose_name_plural = verbose_name


class ProductDocumentModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.FileField(upload_to="product/%Y/%m/%d", storage=MinioBackend(bucket_name='doc'),
                            verbose_name='合同文档')

    class Meta:
        db_table = 'upload_product_document'
        verbose_name = '跟进聊天文档'
        verbose_name_plural = verbose_name


class OrderDocumentModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.FileField(upload_to="order/%Y/%m/%d", storage=MinioBackend(bucket_name='doc'),
                            verbose_name='订单合同')

    class Meta:
        db_table = 'upload_order_document'
        verbose_name = '跟进聊天文档'
        verbose_name_plural = verbose_name


class RecordingModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='文件名')
    file = models.FileField(upload_to="followup/%Y/%m/%d", storage=MinioBackend(bucket_name='audio'),
                            verbose_name='跟进聊天录音')

    class Meta:
        db_table = 'upload_followup_recording'
        verbose_name = '跟进聊天录音'
        verbose_name_plural = verbose_name
