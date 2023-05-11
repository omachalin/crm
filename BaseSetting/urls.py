from rest_framework import routers
from django.urls import path
from .views import BaseSettingViewSet


urlpatterns = []

router = routers.DefaultRouter()

router.register('base-setting', BaseSettingViewSet)

urlpatterns += router.urls
