from .models import (Agreement, Service)
from .serializers import (AgreementSerializer, ServiceSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AgreementFilter
from Coming.pagination import MyPageNumberPagination
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime, time
from django.utils import timezone
from Cashbox.models import Cashbox


class AgreementViewSet(viewsets.ModelViewSet):
  
  filter_backends = (DjangoFilterBackend,)
  filterset_class = AgreementFilter
  pagination_class = MyPageNumberPagination

  queryset = (
    Agreement.objects.annotate(summa=Sum('cashboxes__money'))
    .select_related('coming_fk')
    .select_related('service_fk')
    .order_by('-create_date_time')
  )

  serializer_class = AgreementSerializer


  @action(detail=False, methods=['get'], url_path='get-counter')
  def get_counter(self, request):
    today = timezone.now().date()
    start_of_day = datetime.combine(today, time.min, tzinfo=timezone.utc)
    end_of_day = datetime.combine(today, time.max, tzinfo=timezone.utc)
    agreements_dates_sorted = Agreement.objects.filter(create_date_time__range=(start_of_day, end_of_day))
    money_all = agreements_dates_sorted.aggregate(total=Sum('price'))['total']
    
    payments_cashbox_dates_sorted = Cashbox.objects.filter(
      create_date_time__range=(start_of_day, end_of_day),
      type_payment_fk='b06d0dc1-5698-428d-82ca-e078bb493ee7', # Только оплата по договору
    )

    cashbox_all = payments_cashbox_dates_sorted.aggregate(total=Sum('money'))['total']
    
    dissolution_agreements = Agreement.objects.filter(
      create_date_time__range=(start_of_day, end_of_day),
      dissolution=True
    ).count()

    if not money_all:
      money_all = 0

    if not cashbox_all:
      cashbox_all = 0

    context = {
      'money_all': money_all,
      'cashbox_all': cashbox_all,
      'dissolution_agreements': dissolution_agreements,
    }

    return Response(context)


class ServiceViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated, )
  queryset = Service.objects.all().order_by('-name')
  serializer_class = ServiceSerializer
