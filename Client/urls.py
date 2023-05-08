from rest_framework import routers
from django.urls import path
from .views import ClientViewSet


urlpatterns = [
  
]

router = routers.DefaultRouter()

router.register('client', ClientViewSet)

urlpatterns += router.urls