# Generated by Django 3.2 on 2021-05-06 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopmodel',
            name='create_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='partner',
            field=models.ManyToManyField(blank=True, related_name='customer_partner', to=settings.AUTH_USER_MODEL, verbose_name='合作人'),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shop_own',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_own', to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='shops.categorymodel', verbose_name='上级类别'),
        ),
    ]
