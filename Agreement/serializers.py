from rest_framework import serializers
from Agreement.models import Agreement, Service
from Coming.serializers import ComingSerializer, ComingMinForRateSerializer
from Cashbox.serializers import CashboxSerializer, CashboxMinForRateSerializer

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = (
      'pk',
      'name',
    )


class AgreementMinFromRateSerializer(serializers.ModelSerializer):
  cashboxes = serializers.SerializerMethodField()
  coming = ComingMinForRateSerializer(read_only=True, source='coming_fk')

  def get_cashboxes(self, instance):
    obj = instance.cashboxes.all().order_by('-create_date_time')
    return CashboxMinForRateSerializer(obj, many=True).data

  class Meta:
    model = Agreement
    fields = (
      'pk',
      'number',
      'price_transport',
      'price',
      'cashboxes',
      'coming',
      'create_date_time',
    )

class AgreementSerializer(serializers.ModelSerializer):
  coming = ComingSerializer(read_only=True, source='coming_fk')
  service = ServiceSerializer(read_only=True, source='service_fk')
  cashboxes = serializers.SerializerMethodField()

  def get_cashboxes(self, instance):
    obj = instance.cashboxes.all().order_by('-create_date_time')
    return CashboxSerializer(obj, many=True).data

  class Meta:
    model = Agreement
    fields = (
      'pk',
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
      'create_date_time',
    )
