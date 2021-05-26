from rest_framework.serializers import ModelSerializer
from . import models


class ShopSer(ModelSerializer):
    """
    头像序列化器
    """

    class Meta:
        model = models.ShopModel
        fields = '__all__'
        # fields = ['id', 'name', 'file', 'created_at']
        # read_only_fields = ['created_at']
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     # 这里加不加 都一样 实测接口会将file视为必传参数  但是生成的接口文档里并没有标注这是必传
        #     'file': {'required': True}
        # }
