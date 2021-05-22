from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet


# 单查单增
class RetrieveAndCreateViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    pass
