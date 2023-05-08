from django.shortcuts import render
from Cashbox.models import TypePayment, Cashbox
from Cashbox.serializers import TypePaymentSerializer, CashboxSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from Agreement.models import Agreement
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CashboxFilter


class TypePaymentViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated, )

  queryset = TypePayment.objects.all().order_by('name')
  serializer_class = TypePaymentSerializer


class CashboxViewSet(viewsets.ModelViewSet):
  #permission_classes = (IsAuthenticated, )
  filter_backends = (DjangoFilterBackend,)
  filterset_class = CashboxFilter

  queryset = Cashbox.objects.all()
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
