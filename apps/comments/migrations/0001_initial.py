# Generated by Django 3.2 on 2021-04-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowupCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('reason', models.CharField(default='', max_length=255, verbose_name='评论')),
            ],
            options={
                'verbose_name': '跟进记录评论',
                'verbose_name_plural': '跟进记录评论',
                'db_table': 'crm_followup_comment',
            },
        ),
        migrations.CreateModel(
            name='ShopCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('reason', models.CharField(default='', max_length=255, verbose_name='评论')),
            ],
            options={
                'verbose_name': '店铺评论',
                'verbose_name_plural': '店铺评论',
                'db_table': 'crm_shop_comment',
            },
        ),
    ]
