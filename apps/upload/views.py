from libs.DiyViewSet import RetrieveAndCreateViewSet
from . import models
from . import serializer


class AvatarViewSet(RetrieveAndCreateViewSet):
    """
    头像视图集
    """
    queryset = models.AvatarModel.objects.all()
    serializer_class = serializer.AvatarSer


class ScreenshotViewSet(RetrieveAndCreateViewSet):
    """
    跟进截图视图集
    """
    queryset = models.ScreenshotModel.objects.all()
    serializer_class = serializer.ScreenshotSer


class DocumentViewSet(RetrieveAndCreateViewSet):
    """
    跟进文档视图集
    """
    queryset = models.DocumentModel.objects.all()
    serializer_class = serializer.DocumentSer


class RecordingViewSet(RetrieveAndCreateViewSet):
    """
    跟进录音视图集
    """
    queryset = models.RecordingModel.objects.all()
    serializer_class = serializer.RecordingSer
