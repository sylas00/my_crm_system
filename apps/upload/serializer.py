from rest_framework.serializers import ModelSerializer
from . import models


# 既然他们的模型类都一样 包括字段名 其实可以只写一个序列化器就好了
# 以上想法是错误的 序列化的时候其实都是一样的 但是反序列化的时候 数据会存到序列化器指定的模型类里 所以他们的视图集不能用同一个序列化器

# 想法二  创建一个父类序列化器  再批量继承
# 其实这里的序列化器主要的内容都在 Meta元类里  drf文档说 序列化器默认不继承父类的Meta 除非子类里Meta明确 Meta(父类.Meta)
# 这样才能继承 所以综合来说代码量差不多  那就这样吧 不改动了
class AvatarSer(ModelSerializer):
    """
    头像序列化器
    """

    class Meta:
        model = models.AvatarModel
        fields = ['id', 'name', 'file', 'created_at']
        # read_only_fields = ['created_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            # 这里加不加 都一样 实测接口会将file视为必传参数  但是生成的接口文档里并没有标注这是必传
            'file': {'required': True}
        }


class ScreenshotSer(ModelSerializer):
    """
    跟进截图
    """

    class Meta:
        model = models.ScreenshotModel
        fields = ['id', 'name', 'file', 'created_at']
        read_only_fields = ['created_at']


class OrderImageSer(ModelSerializer):
    """
    订单截图
    """

    class Meta:
        model = models.OrderImageModel
        fields = ['id', 'name', 'file', 'created_at']
        read_only_fields = ['created_at']


class FollowUpDocumentSer(ModelSerializer):
    """
    跟进文档
    """

    class Meta:
        model = models.FollowUpDocumentModel
        fields = ['id', 'name', 'file', 'created_at']
        read_only_fields = ['created_at']


class ProductDocumentSer(ModelSerializer):
    """
    合同文档
    """

    class Meta:
        model = models.ProductDocumentModel
        fields = ['id', 'name', 'file', 'created_at']
        read_only_fields = ['created_at']


class OrderDocumentSer(ModelSerializer):
    """
    订单文档
    """

    class Meta:
        model = models.OrderDocumentModel
        fields = ['id', 'name', 'file', 'created_at']
        read_only_fields = ['created_at']


class RecordingSer(ModelSerializer):
    """
    跟进录音
    """

    class Meta:
        model = models.RecordingModel
        fields = ['id', 'name', 'file', 'created_at']
        read_only_fields = ['created_at']
