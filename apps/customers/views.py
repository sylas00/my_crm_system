from .models import CustomerModel
from .serializer import CustomerSer
from rest_framework.viewsets import ModelViewSet


class CustomerViewSet(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSer
