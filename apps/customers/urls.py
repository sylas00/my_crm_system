from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('customer', views.CustomerViewSet)

urlpatterns = router.urls
