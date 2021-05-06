# Generated by Django 3.2 on 2021-05-06 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '行政区划',
                'verbose_name_plural': '行政区划',
                'db_table': 'crm_areas',
            },
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='客户名')),
                ('qq', models.CharField(blank=True, max_length=255, null=True, verbose_name='QQ')),
                ('wechat', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='座机电话')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='customers.areamodel', verbose_name='地址')),
            ],
            options={
                'verbose_name': '客户表',
                'verbose_name_plural': '客户表',
                'db_table': 'crm_customer',
            },
        ),
    ]
