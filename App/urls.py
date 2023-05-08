from rest_framework import routers
from django.urls import path
from .views import (AppViewSet)

urlpatterns = []
router = routers.DefaultRouter()

router.register('get-app', AppViewSet)

urlpatterns += router.urls