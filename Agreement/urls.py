from rest_framework import routers
from django.urls import path
from .views import AgreementViewSet, ServiceViewSet


urlpatterns = [
  
]

router = routers.DefaultRouter()

router.register('agreement', AgreementViewSet)
router.register('service', ServiceViewSet)

urlpatterns += router.urls