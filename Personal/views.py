from django.shortcuts import render
from .models import Personal, Department, StatusPersone
from .serializers import PersonalSerializer, DepartmentSerializer, StatusPersoneSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class PersonalViewSet(viewsets.ModelViewSet):
  queryset = Personal.objects.all().select_related('department_fk').select_related('status_fk')
  serializer_class = PersonalSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer


class StatusPersoneViewSet(viewsets.ModelViewSet):
  queryset = StatusPersone.objects.all()
  serializer_class = StatusPersoneSerializer

