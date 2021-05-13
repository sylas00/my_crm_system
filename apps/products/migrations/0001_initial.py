# Generated by Django 3.2 on 2021-05-13 06:01

from django.db import migrations, models
import django.db.models.deletion
import django_minio_backend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GiveawayModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='赠品名')),
            ],
            options={
                'verbose_name': '产品赠品',
                'verbose_name_plural': '产品赠品',
                'db_table': 'crm_product_giveaway',
            },
        ),
        migrations.CreateModel(
            name='ProductPlatformModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='产品平台')),
            ],
            options={
                'verbose_name': '产品平台',
                'verbose_name_plural': '产品平台',
                'db_table': 'crm_product_platform',
            },
        ),
        migrations.CreateModel(
            name='ProductTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='产品类型')),
            ],
            options={
                'verbose_name': '产品类型',
                'verbose_name_plural': '产品类型',
                'db_table': 'crm_product_type',
            },
        ),
        migrations.CreateModel(
            name='ServiceTimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='价格')),
                ('service_minimum_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='最低价格')),
                ('service_times', models.IntegerField(blank=True, null=True, verbose_name='数量')),
            ],
            options={
                'verbose_name': '服务次数套餐',
                'verbose_name_plural': '服务次数套餐',
                'db_table': 'crm_product_service_time',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, verbose_name='服务名称')),
                ('package_img', models.ImageField(blank=True, storage=django_minio_backend.models.MinioBackend(bucket_name='image'), upload_to='product/%Y/%m/%d', verbose_name='报价图片')),
                ('contract_file', models.FileField(blank=True, storage=django_minio_backend.models.MinioBackend(bucket_name='doc'), upload_to='product/%Y/%m/%d', verbose_name='合同附件')),
                ('charging_type', models.IntegerField(choices=[(1, '服务周期'), (2, '服务次数')], default=1, verbose_name='收费模式')),
                ('unified_price_year', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='年度统一报价')),
                ('minimum_price_year', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='最低年度报价')),
                ('unified_price_half_year', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='半年统一报价')),
                ('minimum_price_half_year', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='最低半年报价')),
                ('unified_price_quarter', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='季度统一报价')),
                ('minimum_price_quarter', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='最低季度报价')),
                ('unified_price_month', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='月度统一报价')),
                ('minimum_price_month', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='最低月度报价')),
                ('hide', models.BooleanField(default=False, verbose_name='是否隐藏')),
                ('giveaway', models.ManyToManyField(blank=True, related_name='product', to='products.GiveawayModel', verbose_name='赠品')),
                ('platform', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.productplatformmodel', verbose_name='产品平台')),
                ('service_time', models.ManyToManyField(blank=True, related_name='product', to='products.ServiceTimeModel', verbose_name='服务次数套餐')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.producttypemodel', verbose_name='产品类型')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'db_table': 'crm_product_product',
            },
        ),
    ]
