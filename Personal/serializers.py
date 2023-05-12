from .models import (Personal, StatusPersone, Department)
from rest_framework import serializers


class StatusPersoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = StatusPersone
    fields = (
      'pk',
      'name',
    )


class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = (
      'pk',
      'name',
      'create_date',
    )


class PersonalMinForCashBoxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Personal
    fields = (
      'pk',
      'name',
      'pin',
    )


class PersonalSerializer(serializers.ModelSerializer):
  department_fk = DepartmentSerializer()
  status_fk = StatusPersoneSerializer()

  class Meta:
    model = Personal
    fields = (
      'pk',
      'name',
      'phone',
      'department_fk',
      'pin',
      'status_fk',
      'create_date',
    )
