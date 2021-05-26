from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('giveaway', views.GiveawayViewSet)
router.register('service-time', views.ServiceTimeViewSet)
router.register('product-type', views.ProductTypeViewSet)
router.register('product-platform', views.ProductPlatformViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = router.urls
