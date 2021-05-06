from django.db import models

from django_minio_backend import MinioBackend


# 文件表与主体表分离 好处 可以存更多关于文件的信息 坏处 麻烦
class ScreenshotModel(models.Model):
    name = models.CharField(max_length=255, )
    file = models.ImageField(upload_to="followup/%Y/%m/%d", blank=True, storage=MinioBackend(bucket_name='image'),
                             verbose_name='跟进聊天截图')

    class Meta:
        db_table = 'upload_followup_screenshot'
        verbose_name = '跟进聊天截图'
        verbose_name_plural = verbose_name


class DocumentModel(models.Model):
    name = models.CharField(max_length=255, )
    file = models.ImageField(upload_to="followup/%Y/%m/%d", blank=True, storage=MinioBackend(bucket_name='doc'),
                             verbose_name='跟进聊天文档')

    class Meta:
        db_table = 'upload_followup_document'
        verbose_name = '跟进聊天文档'
        verbose_name_plural = verbose_name


class RecordingModel(models.Model):
    name = models.CharField(max_length=255, )
    file = models.ImageField(upload_to="followup/%Y/%m/%d", blank=True, storage=MinioBackend(bucket_name='audio'),
                             verbose_name='跟进聊天录音')

    class Meta:
        db_table = 'upload_followup_recording'
        verbose_name = '跟进聊天录音'
        verbose_name_plural = verbose_name
