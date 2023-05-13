from .models import (Coming, Theme)
from Client.serializers import ClientSerializer
from rest_framework import serializers
from Personal.serializers import PersonalSerializer, PersonalMinForCashBoxSerializer


class ThemeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Theme
    fields = (
      'pk',
      'name',
    )


class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Theme
    fields = (
      'pk',
      'name',
    )


class ComingMinForRateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coming
    fields = (
      'upp',
    )


class ComingMinForCashboxSerializer(serializers.ModelSerializer):
  call_readonly = PersonalMinForCashBoxSerializer(source='call_fk', read_only=True)
  upp_readonly = PersonalMinForCashBoxSerializer(source='upp', read_only=True, many=True)

  class Meta:
    model = Coming
    fields = (
      'call_readonly',
      'upp_readonly',
    )

class ComingSerializer(serializers.ModelSerializer):
  theme = ThemeSerializer(source='theme_fk', read_only=True)
  client = ClientSerializer(source='client_fk', read_only=True)
  status = StatusSerializer(source='status_fk', read_only=True)
  call_readonly = PersonalSerializer(source='call_fk', read_only=True)
  upp_readonly = PersonalSerializer(source='upp', read_only=True, many=True)

  class Meta:
    model = Coming
    fields = (
      'pk',
      'client',
      'client_fk',
      'name',
      #'phone',
      'call_fk',
      'call_readonly',
      'upp',
      'upp_readonly',
      'theme_fk',
      'status_fk',
      'theme',
      'status',
      'create_date_time',
    )