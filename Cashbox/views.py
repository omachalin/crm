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
from .counters import CashBoxCounter
from Coming.pagination import MyPageNumberPagination



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
  pagination_class = MyPageNumberPagination
  queryset = Cashbox.objects.all().select_related(
    'type_money_fk',
    'type_payment_fk'
  ).order_by('-create_date_time')
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
    cashbox_obj = CashBoxCounter()
    cashbox_obj.get_income()
    cashbox_obj.get_expenses()
    cashbox_obj.get_profit()

    return Response(cashbox_obj.get())

  @action(detail=False, methods=['get'], url_path='get-counter-graph')
  def get_counter_graph(self, request):
    cashbox_obj = CashBoxCounter()
    print(cashbox_obj.get_counter_graph())
    return Response(cashbox_obj.get())