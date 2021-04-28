from django.db import models
from django.contrib.auth.models import AbstractUser

from libs.Id_card_validator import id_validator
from django_minio_backend import MinioBackend, iso_date_prefix


class AvatarModel(models.Model):
    file = models.FileField(storage=MinioBackend(bucket_name='django-backend-dev-private'),
                            upload_to= iso_date_prefix, verbose_name='上传')

    class Meta:
        db_table = 'upload_avatar'
        verbose_name = '头像表'
        verbose_name_plural = verbose_name


class User(AbstractUser):
    phone_num = models.CharField(max_length=20, unique=True, blank=True, verbose_name='手机号码', db_index=True)
    real_name = models.CharField(max_length=255, verbose_name='真实姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    id_card = models.CharField(max_length=18, null=True, blank=True, verbose_name='身份证号码', validators=[id_validator])
    birth_date = models.DateField(null=True, blank=True, verbose_name='出生年月日')
    password = models.CharField(max_length=255, blank=True, default='123456', verbose_name='登录密码')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    gender = models.IntegerField(choices=((0, '未设置'), (1, '男'), (2, '女')), default=0, verbose_name='性别')
    status = models.IntegerField(default=1, choices=((1, '考核期'), (2, '试用'), (3, '转正'), (4, '休假'), (5, '离职')),
                                 verbose_name='用户状态')
    is_admin = models.BooleanField(default=False, verbose_name='是否管理员')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='上次登录时间')
    avatar = models.ForeignKey(AvatarModel, on_delete=models.CASCADE, related_name='account', null=True, blank=True,
                               default=1, verbose_name='头像')

    lottery_times = models.IntegerField(default=10, null=True, blank=True, verbose_name='抽奖次数')

    class Meta:
        # 指定一个和系统自带user一样的表名 不知道会不会引发BUG
        db_table = 'auth_user'
        # 指定索引  还一种添加方式是在字段属性加 db_index=True
        indexes = [models.Index(fields=['phone_num', 'username'], name='p_u_idx'), ]
        verbose_name = '员工表'
        verbose_name_plural = verbose_name
