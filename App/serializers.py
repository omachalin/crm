from rest_framework import serializers
from App.models import App


class AppSerializer(serializers.ModelSerializer):
  class Meta:
    model = App
    fields = (
      'pk',
      'name',
      'data',
    )
