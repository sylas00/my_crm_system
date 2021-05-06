# Generated by Django 3.2 on 2021-05-06 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='create_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_create', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='shop',
            field=models.ManyToManyField(blank=True, related_name='customer', to='shops.ShopModel', verbose_name='客户所属店铺'),
        ),
        migrations.AddField(
            model_name='areamodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='customers.areamodel', verbose_name='上一级行政区'),
        ),
    ]
