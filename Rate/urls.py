from rest_framework import routers
from django.urls import path
from .views import GetRate


urlpatterns = [
  path('get-rate/', GetRate.as_view()),
]

router = routers.DefaultRouter()

# router.register('type-payment', TypePaymentViewSet)
# router.register('type-money', TypeMoneyViewSet)
# router.register('cashbox', CashboxViewSet)

urlpatterns += router.urls
