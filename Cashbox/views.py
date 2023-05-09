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
from datetime import datetime, time
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum


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
    expenses_status = '6619e12f-3247-4aea-93bf-434059ec6182'
    cashbox_today = Cashbox.objects.filter(
      create_date_time__date=today,
    ).exclude(type_payment_fk=expenses_status).aggregate(total=Sum('money'))['total'] or 0
    cashbox_15_days = Cashbox.objects.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=fifteen_days_ago
    ).exclude(type_payment_fk=expenses_status).aggregate(total=Sum('money'))['total'] or 0
    cashbox_month = Cashbox.objects.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=month_ago
    ).exclude(type_payment_fk=expenses_status).aggregate(total=Sum('money'))['total'] or 0

    # agreements_dates_sorted = Agreement.objects.filter(create_date_time__range=(start_of_day, end_of_day))
    # money_all = agreements_dates_sorted.aggregate(total=Sum('price'))['total']
    
    # payments_cashbox_dates_sorted = Cashbox.objects.filter(
    #   create_date_time__range=(start_of_day, end_of_day),
    #   type_payment_fk='b06d0dc1-5698-428d-82ca-e078bb493ee7', # Только оплата по договору
    # )

    # cashbox_all = payments_cashbox_dates_sorted.aggregate(total=Sum('money'))['total']
    
    # dissolution_agreements = Agreement.objects.filter(
    #   create_date_time__range=(start_of_day, end_of_day),
    #   dissolution=True
    # ).count()

    # if not money_all:
    #   money_all = 0

    # if not cashbox_all:
    #   cashbox_all = 0

    context = {
      'cashbox_today': cashbox_today,
      'cashbox_month': cashbox_month,
      'cashbox_15_days': cashbox_15_days,
    }

    return Response(context)