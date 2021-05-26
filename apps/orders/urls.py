from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('order', views.OrderViewSet)

urlpatterns = router.urls
