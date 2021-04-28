# Generated by Django 3.2 on 2021-04-28 12:53

from django.db import migrations, models
import django_minio_backend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django_minio_backend.models.MinioBackend(bucket_name='django-backend-dev-private'), upload_to=django_minio_backend.models.iso_date_prefix, verbose_name='上传')),
            ],
            options={
                'verbose_name': '头像表',
                'verbose_name_plural': '头像表',
                'db_table': 'upload_avatar',
            },
        ),
    ]
