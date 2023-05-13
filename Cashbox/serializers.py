from rest_framework import serializers
from Cashbox.models import TypePayment, Cashbox, TypeMoney
from Coming.serializers import ComingMinForCashboxSerializer
from Agreement.models import Agreement


class TypePaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = TypePayment
    fields = (
      'pk',
      'name',
    )

class TypeMoneySerializer(serializers.ModelSerializer):
  class Meta:
    model = TypeMoney
    fields = (
      'pk',
      'name',
    )


class AgreementMinSerializer(serializers.ModelSerializer):
   coming = ComingMinForCashboxSerializer(read_only=True, source='coming_fk')

   class Meta:
    model = Agreement
    fields = (
      'number',
      'coming',
      'price',
      'create_date_time',
    )


class CashboxSerializer(serializers.ModelSerializer):
  type_payment = TypePaymentSerializer(read_only=True, source='type_payment_fk')
  type_money = TypeMoneySerializer(read_only=True, source='type_money_fk')
  agreements = AgreementMinSerializer(read_only=True, many=True, source='agreement_set')

  class Meta:
    model = Cashbox
    fields = (
      'pk',
      'name',
      'money',
      'type_payment_fk',
      'type_money_fk',
      'type_money',
      'type_payment',
      'create_date_time',
      'agreements',
    )
    ordering = ['-money']
