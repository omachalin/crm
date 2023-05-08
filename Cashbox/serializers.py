from rest_framework import serializers
from Cashbox.models import TypePayment, Cashbox


class TypePaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = TypePayment
    fields = (
      'pk',
      'name',
    )


class CashboxSerializer(serializers.ModelSerializer):
  type_payment = TypePaymentSerializer(read_only=True, source='type_payment_fk')
  class Meta:
    model = Cashbox
    fields = (
      'pk',
      'name',
      'money',
      'type_payment_fk',
      'type_payment',
      'create_date_time',
    )
    ordering = ['-money']