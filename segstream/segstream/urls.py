import environ
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('myusers.urls')),
    path('api/v1/', include('apilogs.urls')),
]

env = environ.Env()
DEBUG = True

if DEBUG:
    urlpatterns.append(
        path('api/v1/docs/', include('apps.swagdoc.urls'))
    )