from rest_framework.serializers import ModelSerializer
from . import models


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


class DocumentSer(ModelSerializer):
    """
    跟进文档
    """

    class Meta:
        model = models.DocumentModel
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
