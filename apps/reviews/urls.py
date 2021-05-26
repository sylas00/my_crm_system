from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('shop-review', views.ShopReviewViewSet)
router.register('followup-review', views.FollowupReviewViewSet)
router.register('order-review', views.OrderReviewViewSet)

urlpatterns = router.urls
