from rest_framework.routers import DefaultRouter
from .views import SegstreamAPILogsAPIView

router = DefaultRouter()
router.register('api-logs', SegstreamAPILogsAPIView, basename='api-logs')

urlpatterns = []
urlpatterns += router.urls
