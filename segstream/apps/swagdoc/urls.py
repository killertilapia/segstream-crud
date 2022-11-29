from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="segstream_api",
      default_version='v1',
      description="SegStream REST API",
      terms_of_service="https://www.segstream.com/en-us/about/legal-information/",
      contact=openapi.Contact(email="it_support@segstream.com"),
      license=openapi.License(name="MIT License"),
   ),
   url='http://localhost:8000',
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]