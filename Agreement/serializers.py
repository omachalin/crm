from rest_framework import serializers
from Agreement.models import Agreement, Service
from Coming.serializers import ComingSerializer
from Cashbox.serializers import CashboxSerializer

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = (
      'pk',
      'name',
    )


class AgreementSerializer(serializers.ModelSerializer):
  coming = ComingSerializer(read_only=True, source='coming_fk')
  service = ServiceSerializer(read_only=True, source='service_fk')
  cashboxes = serializers.SerializerMethodField()
  #paid_money  = serializers.SerializerMethodField()
  #paid_transport  = serializers.SerializerMethodField()
  
  # def get_paid_money(self, obj):
  #   return obj.cashboxes.filter(
  #     type_payment_fk__pk='8e886f31-5400-4a0d-86cc-56893dfac269'
  #   ).aggregate(models.Sum('money'))['money__sum']

  # def get_paid_transport(self, obj):
  #   return obj.cashboxes.filter(
  #     type_payment_fk__pk='7bbcda1a-38b4-49fa-ab81-adf076c45b8e'
  #   ).aggregate(models.Sum('money'))['money__sum']

  def get_cashboxes(self, instance):
    obj = instance.cashboxes.all().order_by('-create_date_time')
    return CashboxSerializer(obj, many=True).data

  class Meta:
    model = Agreement
    fields = (
      'pk',
      #'paid_money',
      #'paid_transport',
      'number',
      'coming_fk',
      'coming',
      'price',
      'price_transport',
      'service_fk',
      'service',
      'note',
      'dissolution',
      'cashboxes',
      #'cashboxes_set',
      'create_date_time',
    )
