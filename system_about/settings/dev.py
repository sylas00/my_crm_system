"""
Django settings for system_about project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/

从 global_settings.py 载入默认设置.
从指定的 settings 文件载入用户设置, 需要时覆盖掉默认设置.
"""
import os
from pathlib import Path
import sys
from datetime import timedelta
from typing import List, Tuple

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# BASE_DIR 指的就是manager文件所在的路径 由于我自行修改了路径 所以要再加一个parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 增加一个apps包的导包路径
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i9zm=v$+f#ihdcifq2z$5p87keq8b*fyg+80&-4x#4wg!(=0_t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    # 自动寻找每个app里的admin并导入
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # minio储存后端
    'django_minio_backend',
    # 软删除
    'softdelete',
    # DRF
    'rest_framework',
    # 文档
    "drf_yasg",

    ############
    'users',
    'shops',
    'customers',
    'followups',
    'orders',
    'comments',
    'payment',
    'products',
    'reviews',
    'upload',

]

# 指定一下自定义user作为系统的user
AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'system_about.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'system_about.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'learnsql',
        'HOST': '127.0.0.1',
        'PASSWORD': '123456',
        'USER': 'xujin',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# 当使用时区时，Django存储在数据库中的所有日期时间信息都以UTC时区为准，在后台使用有时区的datetime，前台用户使用时，在网页上翻译成用户所在的时区。
# TIME_ZONE的作用是在模板渲染的时候转化时间用的
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True

USE_L10N = True

# 使用时区 数据库存储的时间都是UTC时间
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# minio相关配置
# 连接后端
MINIO_ENDPOINT = 'localhost:9000'
MINIO_ACCESS_KEY = 'minioadmin'
MINIO_SECRET_KEY = 'minioadmin'
MINIO_USE_HTTPS = False
MINIO_URL_EXPIRY_HOURS = timedelta(days=1)
MINIO_CONSISTENCY_CHECK_ON_START = True
# 配置里必须要有公开和私有这两个配置
MINIO_PRIVATE_BUCKETS = [
    'privatefile',
]
MINIO_PUBLIC_BUCKETS = [
    'video',
    'image',
    'doc',
    'audio',

]
MINIO_POLICY_HOOKS: List[Tuple[str, dict]] = []
# 在文件储存的字段里定义储存后端为MinioBackend之后 他会自动解决文件重名问题 如果是自定义的文件 要重写文件上传的save方法 不然会导致文件覆盖
# upload_to指定上传文件路径 需要如下配置一下 如果和储存后端upload_to都不指定 文件就会默认存在运行目录
# 媒体文件位置
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DRF配置
REST_FRAMEWORK = {
    # 权限配置
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 指定simplejwt认证后端
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# 配置jwt认证 本项目用的是djangorestframework-simplejwt 支持3.1 djangorestframework-jwt只支持到django2.x 而且很久没更新
# jwt包含三个部分
# header(alg:算法 typ:类型)

# payload(
# iss (issuer)：签发人
# exp (expiration time)：过期时间
# sub (subject)：主题
# aud (audience)：受众
# nbf (Not Before)：生效时间
# iat (Issued At)：签发时间
# jti (JWT ID)：编号)

# Signature 签名 防篡改
# 访问令牌和刷新令牌的区别 为了服务端可以更及时地修改用户的权限或者其他能够更快生效 如果只有一个令牌 那时间将会固定死
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=300),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=300),
    # 用jwt登录自动刷新更新最后登录时间
    'UPDATE_LAST_LOGIN': True,

    'AUTH_HEADER_TYPES': ('Bearer',),
    # 在数据库中 储存用户唯一标识的字段 的字段名(最好用id 不用用户名和邮箱之类的 因为可能会变)  将会默认在jwt的payload 部分中
    'USER_ID_FIELD': 'id',
    # 在payload中 给上面这个数据的命名
    'USER_ID_CLAIM': 'user_id',
}
