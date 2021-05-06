from django.db import models
from django.contrib.auth.models import AbstractUser
from django_minio_backend import MinioBackend

from libs.Id_card_validator import id_validator
from libs.soft_delete_model import BaseModel


# 超级大坑 继承类的顺序不一样也会报错 后者不能排前面 不然就要自定义管理器 相当于官方文档第三种拓展用户类的方法
# 然后 官方文档方法2和方法3的区别（取决于是否修改或重写原有字段？）
class User(AbstractUser, BaseModel):
    GENDER_CHOICES = [
        (0, '未知'),
        (1, '男'),
        (2, '女')
    ]
    STATUS_CHOICES = [
        (1, '试用'),
        (2, '转正'),
        (3, '休假'),
        (4, '离职')
    ]
    phone_num = models.CharField(max_length=20, unique=True, blank=True, verbose_name='手机号码', db_index=True)
    real_name = models.CharField(max_length=255, verbose_name='真实姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    id_card = models.CharField(max_length=18, null=True, blank=True, verbose_name='身份证号码', validators=[id_validator])
    birth_date = models.DateField(null=True, blank=True, verbose_name='出生年月日')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    status = models.IntegerField(default=1, choices=STATUS_CHOICES, verbose_name='用户状态')
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True,
                               storage=MinioBackend(bucket_name='image'), verbose_name='头像')
    lottery_times = models.IntegerField(default=10, null=True, blank=True, verbose_name='抽奖次数')

    class Meta:
        # 指定一个和系统自带user一样的表名 不知道会不会引发BUG
        db_table = 'auth_user'
        # 指定索引  还一种添加方式是在字段属性加 db_index=True
        indexes = [models.Index(fields=['phone_num', 'username'], name='p_u_idx'), ]
        verbose_name = '员工表'
        verbose_name_plural = verbose_name
