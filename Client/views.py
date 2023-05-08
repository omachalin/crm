from django.shortcuts import render
from .models import (Client)
from .serializers import (ClientSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class ClientViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated, )
  #filter_backends = (DjangoFilterBackend,)
  #filterset_class = ComingFilter
  #pagination_class = MyPageNumberPagination

  queryset = Client.objects.all()
  serializer_class = ClientSerializer

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
    else:
      queryset = Client.objects.filter(phone=request.data['phone']).first()
      serializer = ClientSerializer(queryset)
      headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=200, headers=headers)
