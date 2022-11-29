from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

User = get_user_model()

# Create your views here.
class SegstreamUserAPIView(ModelViewSet):
    """
    Users CRUD API
    """
    permission_classes = [permissions.AllowAny]

    queryset = User.objects.all()
    serializer_class = UserSerializer

