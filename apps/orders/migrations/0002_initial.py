# Generated by Django 3.2 on 2021-04-30 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='founder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='helper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_helper', to=settings.AUTH_USER_MODEL, verbose_name='帮谈人'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='shops.shopmodel', verbose_name='关联店铺'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='whether_to_cooperate_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whether_to_cooperate_person', to=settings.AUTH_USER_MODEL, verbose_name='合作转接人'),
        ),
    ]
