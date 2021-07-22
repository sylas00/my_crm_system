from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    # path('user/', views.UserGroup),
    path('useraaa/', views.Useraaa.as_view()),
]
urlpatterns += router.urls
