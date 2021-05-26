from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('payment', views.PaymentViewSet)

urlpatterns = router.urls
