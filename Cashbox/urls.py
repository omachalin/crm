from rest_framework import routers
from django.urls import path
from .views import TypePaymentViewSet, CashboxViewSet


urlpatterns = [
  
]

router = routers.DefaultRouter()

router.register('type-payment', TypePaymentViewSet)
router.register('cashbox', CashboxViewSet)

urlpatterns += router.urls
