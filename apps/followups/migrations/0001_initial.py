# Generated by Django 3.2 on 2021-04-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('follow_way', models.SmallIntegerField(choices=[(0, '未知'), (1, '电话'), (2, '微信'), (3, 'QQ'), (4, '面谈')], default=0, verbose_name='跟进方式')),
                ('follow_time', models.DateTimeField(blank=True, null=True, verbose_name='跟进时间')),
                ('follow_next_time', models.DateTimeField(blank=True, null=True, verbose_name='预计下次跟进时间')),
                ('chat_record', models.TextField(blank=True, default=None, null=True, verbose_name='聊天记录')),
                ('follow_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='跟进情况描述')),
                ('marking', models.SmallIntegerField(choices=[(0, '不打标'), (1, '新加意向'), (2, '回访意向'), (3, '合作转接'), (4, '特殊延伸'), (5, '客户跟踪'), (6, '成交')], default=0, verbose_name='绩效打标')),
                ('intentional', models.IntegerField(choices=[(0, '未知'), (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')], default=1, verbose_name='意向度')),
                ('estimated_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='预估金额')),
                ('estimated_date', models.DateField(blank=True, null=True, verbose_name='预估日期')),
                ('sales_stage', models.SmallIntegerField(choices=[(0, '未知'), (1, '成功开场'), (2, '业绩介绍'), (3, '解答问题'), (4, '约定付款'), (5, '成交')], default=0, verbose_name='销售阶段')),
            ],
            options={
                'verbose_name': '跟进记录表',
                'verbose_name_plural': '跟进记录表',
                'db_table': 'crm_followup',
            },
        ),
        migrations.CreateModel(
            name='SalesStageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('stage_name', models.CharField(max_length=255, verbose_name='销售阶段')),
            ],
            options={
                'verbose_name': '销售阶段表',
                'verbose_name_plural': '销售阶段表',
                'db_table': 'crm_sales_stage',
            },
        ),
    ]
