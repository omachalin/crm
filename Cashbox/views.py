from django.shortcuts import render
from Cashbox.models import TypePayment, Cashbox, TypeMoney
from Cashbox.serializers import TypePaymentSerializer, CashboxSerializer, TypeMoneySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from Agreement.models import Agreement
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CashboxFilter
from datetime import datetime, timedelta
from django.db.models import Sum
from BaseSetting.get_setting import get_options
from django.db.models.functions import Coalesce

class TypePaymentViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated, )
  queryset = TypePayment.objects.all().order_by('name')
  serializer_class = TypePaymentSerializer


class TypeMoneyViewSet(viewsets.ModelViewSet):
  #permission_classes = (IsAuthenticated, )
  queryset = TypeMoney.objects.all().order_by('name')
  serializer_class = TypeMoneySerializer


class CashboxViewSet(viewsets.ModelViewSet):
  #permission_classes = (IsAuthenticated, )
  filter_backends = (DjangoFilterBackend,)
  filterset_class = CashboxFilter

  queryset = Cashbox.objects.all().select_related('type_money_fk', 'type_payment_fk')
  serializer_class = CashboxSerializer

  @action(detail=False, methods=['post'], url_path='add-payment-agreement')
  def add_payment_agreement(self, request):
    data = request.data
    serializer = CashboxSerializer(data=data)
    if serializer.is_valid():
      agreement_fk = data['agreement_fk']
      del data['agreement_fk']
      request.data['type_payment_fk'] = TypePayment.objects.filter(pk=data['type_payment_fk']).first()
      Cashbox.objects.create(**request.data)
      last_payment = Cashbox.objects.latest('create_date_time')
      serializer = CashboxSerializer(last_payment)
      agreement = Agreement.objects.filter(pk=agreement_fk).first()
      agreement.cashboxes.add(last_payment)
      agreement.save()
    else:
      raise Exception(serializer.errors)
    return Response(serializer.data)

  @action(detail=False, methods=['get'], url_path='get-counter')
  def get_counter(self, request):
    today = datetime.today().date()
    fifteen_days_ago = today - timedelta(days=15)
    month_ago = today - timedelta(days=30)
    base_settings = get_options(['cashbox_type_payment_fk_expenses_status'])

    cashbox = Cashbox.objects.exclude(type_payment_fk=base_settings['cashbox_type_payment_fk_expenses_status'])
    cashbox_today = cashbox.filter(create_date_time__date=today).aggregate(
      total=Coalesce(Sum('money'), 0)
    )['total']

    cashbox_15_days = cashbox.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=fifteen_days_ago
    ).aggregate(total=Coalesce(Sum('money'), 0))['total']

    cashbox_month = cashbox.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=month_ago
    ).aggregate(total=Coalesce(Sum('money'), 0))['total']

    context = {
      'cashbox_today': cashbox_today,
      'cashbox_month': cashbox_month,
      'cashbox_15_days': cashbox_15_days,
    }

    return Response(context)