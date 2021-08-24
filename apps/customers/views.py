import django_filters

from .models import CustomerModel
from .serializer import CustomerSer
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters


class CustomerFilter(filters.FilterSet):
    # 自己定义过滤
    # 查询参数的名字                                字段名字             条件
    my_define_id = filters.NumberFilter(field_name="id", lookup_expr='gte')

    # 实现排序
    # 查询参数的名字                         要实现排序的字段名
    order = filters.OrderingFilter(fields=('name', 'created_at'))

    class Meta:
        model = CustomerModel
        # 同时指定多个字段 但只支持精确查找
        # fields = ['id', 'name']

        # 同时指定多个字段 并自选增加field查找条件 django文档中所有查找条件
        # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups
        fields = {
            # 'id': ['lt', 'gt', 'exact', 'gte', ],
            'name': ['exact', 'contains', "istartswith", ],
            # 且支持跨关系
            'shop__name': ['exact']
        }


class CustomerViewSet(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSer

    # 请注意，不支持同时使用filterset_fields和filterset_class。

    # 使用drf的filter后端
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name','id',)

    # 使用django-filter后端
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilter
