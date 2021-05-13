# Generated by Django 3.2 on 2021-05-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('channel', models.CharField(blank=True, max_length=255, verbose_name='付款渠道')),
                ('name', models.TextField(blank=True, verbose_name='账户/名称')),
                ('method', models.CharField(blank=True, max_length=255, verbose_name='支付方式')),
                ('remark', models.TextField(blank=True, verbose_name='备注说明')),
                ('hide', models.BooleanField(default=False, verbose_name='是否隐藏')),
            ],
            options={
                'verbose_name': '付款方式',
                'verbose_name_plural': '付款方式',
                'db_table': 'crm_payment',
            },
        ),
    ]
