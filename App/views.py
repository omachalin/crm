from django.shortcuts import render
from rest_framework import viewsets
from App.models import App
from App.serializers import AppSerializer


class AppViewSet(viewsets.ModelViewSet):
  queryset = App.objects.all()
  serializer_class = AppSerializer
