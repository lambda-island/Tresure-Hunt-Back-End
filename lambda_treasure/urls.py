from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import testing

urlpatterns = [
    path('', testing, name='testing'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/',
         TokenObtainPairView.as_view(),
         name="token-obtain-pair"),
    path('api/auth/verify/',
         TokenVerifyView.as_view(),
         name="token=verification"),
    path('api/auth/refresh/',
         TokenRefreshView.as_view(),
         name="token-refresh"),
]