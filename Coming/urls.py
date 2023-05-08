from rest_framework import routers
from django.urls import path
from .views import (ComingViewSet, ThemeViewSet, StatusViewSet, CloneComing, CounterComing)


urlpatterns = [
  path('coming-clone/<uuid:uuid>/', CloneComing.as_view()),
  path('counter-coming/', CounterComing.as_view()),
]
router = routers.DefaultRouter()

router.register('get-coming', ComingViewSet)
router.register('get-theme', ThemeViewSet)
router.register('get-status', StatusViewSet)

urlpatterns += router.urls