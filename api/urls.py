from django.urls import path, include
from rest_framework import routers

from api.views import TaskViewSet, TagViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
