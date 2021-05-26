from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('followup-comment', views.FollowupCommentViewSet)
router.register('shop-comment', views.ShopCommentViewSet)

urlpatterns = router.urls
