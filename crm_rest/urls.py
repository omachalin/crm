from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

schema_view = get_schema_view(
  openapi.Info(
    title="Snippets API",
    default_version='v1',
    description="Test description",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/v1/auth/', include('Auth.urls')),
    re_path(r'^api/v1/coming/', include('Coming.urls')),
    re_path(r'^api/v1/personal/', include('Personal.urls')),
    re_path(r'^api/v1/app/', include('App.urls')),
    re_path(r'^api/v1/agreement/', include('Agreement.urls')),
    re_path(r'^api/v1/basesetting/', include('BaseSetting.urls')),
    re_path(r'^api/v1/rate/', include('Rate.urls')),
    re_path(r'^api/v1/client/', include('Client.urls')),
    re_path(r'^api/v1/cashbox/', include('Cashbox.urls')),
    re_path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'), 
    re_path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name =' token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
