from .models import (Coming, Theme)
from Client.serializers import ClientSerializer
from rest_framework import serializers


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


class ComingSerializer(serializers.ModelSerializer):
  theme = ThemeSerializer(source='theme_fk', read_only=True)
  client = ClientSerializer(source='client_fk', read_only=True)
  status = StatusSerializer(source='status_fk', read_only=True)

  class Meta:
    model = Coming
    fields = (
      'pk',
      'client',
      'client_fk',
      'name',
      #'phone',
      'call',
      'upp',
      'theme_fk',
      'status_fk',
      'theme',
      'status',
      'create_date_time',
    )