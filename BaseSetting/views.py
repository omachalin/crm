from django.shortcuts import render
from BaseSetting.serializer import BaseSettingSerializer
from BaseSetting.models import BaseSetting
from rest_framework import viewsets
from Coming.pagination import MyPageNumberPagination
from .filters import BaseSettingFilter


class BaseSettingViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  pagination_class = MyPageNumberPagination
  filterset_class = BaseSettingFilter

  queryset = BaseSetting.objects.all().select_related('app_fk')
  serializer_class = BaseSettingSerializer
