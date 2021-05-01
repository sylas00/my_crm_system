# Generated by Django 3.2 on 2021-04-30 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followups', '0002_initial'),
        ('shops', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopreviewmodel',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='shopreviewmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='shops.shopmodel', verbose_name='关联店铺'),
        ),
        migrations.AddField(
            model_name='orderreviewmodel',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='orderreviewmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='orders.ordermodel', verbose_name='关联订单'),
        ),
        migrations.AddField(
            model_name='followupreviewmodel',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AddField(
            model_name='followupreviewmodel',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='followups.followupmodel', verbose_name='关联跟进'),
        ),
    ]