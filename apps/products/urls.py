from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
# router.register('followup', views.FollowUpViewSet)

urlpatterns = router.urls
