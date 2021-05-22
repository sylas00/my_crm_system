"""system_about URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="HelloDjango REST framework tutorial API",
        default_version="v1",
        description="HelloDjango REST framework tutorial AP",
        terms_of_service="",
        contact=openapi.Contact(email="zmrenwu@163.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# url 要加斜杠 不然 my 在 mysite 之前  框架无法识别 只能按照顺序先选择my
urlpatterns = [
    # django自带管理后端
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    # jwt认证和刷新 最后还是决定不用 自定义的验证
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # drf 自动接口文档
    # 本来想使用传统的coreapi 实现自动生成接口文档 在stackoverflow看到文章说应该改用openapi
    #  coreapi只是drf曾经的标准 而openapi是api服务的标准 相当于 django里的模型类  和 sql语句的区别  所以决定使用drf-yasg
    re_path(r"swagger(?P<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json", ),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui", ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    path('', include('users.urls')),
    path('upload/', include('upload.urls')),
]
