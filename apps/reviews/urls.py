from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('followup', views.ShopReviewViewSet)
router.register('followup', views.FollowupReviewViewSet)
router.register('followup', views.OrderReviewViewSet)

urlpatterns = router.urls
