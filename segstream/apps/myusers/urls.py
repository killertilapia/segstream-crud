from rest_framework.routers import DefaultRouter
from .views import SegstreamUserAPIView

router = DefaultRouter()
router.register('users', SegstreamUserAPIView, basename='users')

urlpatterns = []
urlpatterns += router.urls
