# Generated by Django 3.2 on 2021-04-30 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='类目名称')),
            ],
            options={
                'verbose_name': '店铺类目表',
                'verbose_name_plural': '店铺类目表',
                'db_table': 'crm_shop_store_category',
            },
        ),
        migrations.CreateModel(
            name='ShopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='店铺名')),
                ('url', models.URLField(blank=True, default='', max_length=1024, verbose_name='店铺链接')),
                ('product_quantity', models.IntegerField(blank=True, null=True, verbose_name='产品数量')),
                ('cumulative_sales', models.IntegerField(blank=True, null=True, verbose_name='累计销售量')),
                ('sales', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='销售额')),
                ('shop_opening_time', models.DateField(blank=True, null=True, verbose_name='开店时间')),
                ('locked', models.BooleanField(default=False, verbose_name='锁定客户')),
                ('lock_time', models.DateTimeField(blank=True, null=True, verbose_name='锁定时间')),
                ('add_partner_time', models.DateTimeField(blank=True, null=True, verbose_name='添加合作人时间')),
                ('customer_source', models.SmallIntegerField(choices=[(0, '未知'), (1, '独立开发'), (2, '指定分配'), (3, '同事转接')], default=0, verbose_name='店铺来源')),
                ('followup_method', models.SmallIntegerField(choices=[(0, '未知'), (1, '电话沟通'), (2, '网络沟通'), (3, '面谈')], default=0, verbose_name='主要跟进方式')),
                ('platform', models.SmallIntegerField(choices=[(0, '未知'), (1, '淘宝'), (2, '天猫'), (3, '京东'), (4, '拼多多'), (5, '亚马逊')], default=0, verbose_name='店铺平台')),
                ('is_close', models.BooleanField(default=False, verbose_name='是否关店')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='shops.categorymodel', verbose_name='店铺类目')),
            ],
            options={
                'verbose_name': '客户店铺信息表',
                'verbose_name_plural': '客户店铺信息表',
                'db_table': 'crm_shop',
            },
        ),
    ]
