from drf_api_logger.models import APILogsModel
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import APILogsSerializer

# Create your views here.
class SegstreamAPILogsAPIView(ReadOnlyModelViewSet):
    """
    API Logs API - Read Only
    """
    permission_classes = [permissions.AllowAny]

    queryset = APILogsModel.objects.all()
    serializer_class = APILogsSerializer