from rest_framework import serializers
from BaseSetting.models import BaseSetting
from App.serializers import AppSerializer


class BaseSettingSerializer(serializers.ModelSerializer):
  app = AppSerializer(read_only=True, source='app_fk')

  class Meta:
    model = BaseSetting
    fields = (
      'id',
      'name',
      'value',
      'value',
      'description',
      'app_fk',
      'app',
    )
