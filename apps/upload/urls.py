from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# router = SimpleRouter(trailing_slash=False)# 末尾不加斜杠

# 默认加 和django的append_slash 一样 在get请求中 /1/ 和 /1 一样 但是post 就只能/1/
router = SimpleRouter()
# 这里的路由就不加/了
router.register('avatar', views.AvatarViewSet)
router.register('screenshot', views.ScreenshotViewSet)
router.register('order-image', views.OrderImageViewSet)
router.register('followup-document', views.FollowUpDocumentViewSet)
router.register('product-document', views.ProductDocumentViewSet)
router.register('order-document', views.OrderDocumentViewSet)
router.register('recording', views.RecordingViewSet)

urlpatterns = router.urls
