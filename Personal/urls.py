from rest_framework import routers
from django.urls import path
from .views import (PersonalViewSet, DepartmentViewSet, StatusPersoneViewSet)

urlpatterns = []

router = routers.DefaultRouter()

router.register('get-personal', PersonalViewSet)
router.register('get-department', DepartmentViewSet)
router.register('get-status-persone', StatusPersoneViewSet)

urlpatterns += router.urls