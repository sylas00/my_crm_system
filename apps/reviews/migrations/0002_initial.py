# Generated by Django 3.2 on 2021-05-06 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0001_initial'),
        ('followups', '0002_initial'),
        ('reviews', '0001_initial'),
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopreviewmodel',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_review', to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='shopreviewmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='shops.shopmodel', verbose_name='关联店铺'),
        ),
        migrations.AddField(
            model_name='orderreviewmodel',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_review', to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='orderreviewmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='orders.ordermodel', verbose_name='关联订单'),
        ),
        migrations.AddField(
            model_name='followupreviewmodel',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followup_review', to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='followupreviewmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='followups.followupmodel', verbose_name='关联跟进'),
        ),
    ]
