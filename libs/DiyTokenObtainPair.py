# 这个模块并未被使用
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView


# 思考 好像都不用改 大多数判断逻辑 都由后端完成

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # 这是simplejwt的官方文档里说的自定义返回值的方式 能返回用户更多信息 但是信息都在jwt的payload中
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

    # 这是网上比较多教程 直接把用户信息 返回   跟上面比 哪种更好？
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # data['username'] = self.user.username

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
