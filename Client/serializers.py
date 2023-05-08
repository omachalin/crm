from .models import (Client)
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = (
      'pk',
      'name',
      'phone',
      'create_date_time',
    )