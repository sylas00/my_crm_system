from django.db import models

# Create your mod


from django_minio_backend import MinioBackend, iso_date_prefix


class AvatarModel(models.Model):
    file = models.FileField(storage=MinioBackend(bucket_name='django-backend-dev-private'),
                            upload_to=iso_date_prefix, verbose_name='上传')

    class Meta:
        db_table = 'upload_avatar'
        verbose_name = '头像表'
        verbose_name_plural = verbose_name
