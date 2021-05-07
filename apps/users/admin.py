from django.contrib import admin

# Register your models here.
from .models import User


# 方法一 直接注册要管理的模型类
# admin.site.register(User)

# 方法二
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    # 自选在页面管理中的字段
    # fields = ['username', 'last_login']
    # 将字段用元组包裹 可以视他们在页面展示的时候在同一行
    # fields = [('username', 'last_login')]
    # 不在页面管理中存在的字段
    # exclude = ['fields']
