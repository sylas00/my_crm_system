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


class OrderImageViewSet(RetrieveAndCreateViewSet):
    """
    跟进截图视图集
    """
    queryset = models.OrderImageModel.objects.all()
    serializer_class = serializer.OrderImageSer


class FollowUpDocumentViewSet(RetrieveAndCreateViewSet):
    """
    跟进文档视图集
    """
    queryset = models.FollowUpDocumentModel.objects.all()
    serializer_class = serializer.FollowUpDocumentSer


class ProductDocumentViewSet(RetrieveAndCreateViewSet):
    """
    跟进文档视图集
    """
    queryset = models.ProductDocumentModel.objects.all()
    serializer_class = serializer.ProductDocumentSer


class OrderDocumentViewSet(RetrieveAndCreateViewSet):
    """
    跟进文档视图集
    """
    queryset = models.OrderDocumentModel.objects.all()
    serializer_class = serializer.OrderDocumentSer


class RecordingViewSet(RetrieveAndCreateViewSet):
    """
    跟进录音视图集
    """
    queryset = models.RecordingModel.objects.all()
    serializer_class = serializer.RecordingSer
