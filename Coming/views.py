from django.shortcuts import render
from .models import Coming, Theme, Status
from Agreement.models import Agreement
from .serializers import ComingSerializer, ThemeSerializer, StatusSerializer
from rest_framework import viewsets
from .filters import ComingFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .pagination import MyPageNumberPagination
from django.http import JsonResponse
from .get_counter import Counter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class ComingViewSet(viewsets.ModelViewSet):
  #permission_classes = (IsAuthenticated, )
  filter_backends = (DjangoFilterBackend,)
  filterset_class = ComingFilter
  pagination_class = MyPageNumberPagination

  queryset = (Coming.objects.all()
              .select_related('theme_fk', 'status_fk', 'call_fk').prefetch_related('upp')
              .order_by('-create_date_time'))
  serializer_class = ComingSerializer

  def replace_client_key(self, data):
    for key in data:
      key['phone'] = key['client']['phone']
      del key['client']
    return data

  @action(detail=False, methods=['GET'])
  def get_coming_with_client(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(self.replace_client_key(serializer.data))
    serializer = self.get_serializer(queryset, many=True)
    
    return Response(self.replace_client_key(serializer.data))

  def update(self, request, *args, **kwargs):
    super().update(request, *args, **kwargs)
    instance = self.get_object()

    if not Agreement.objects.filter(coming_fk=instance):
      status_agreement = Status.objects.filter(name='Договор').first()
      if instance.status_fk.pk == status_agreement.pk:
        last_agreement = Agreement.objects.first()
        Agreement.objects.create(number=int(last_agreement.number) + 1, coming_fk=instance)

    serializer = ComingSerializer(instance)
    return Response(serializer.data)


class CounterComing(APIView):
  permission_classes = (IsAuthenticated, )
  def get(self, request, *args, **kwargs):
    obj = Counter()
    obj.set_min_max_date()
    return JsonResponse(obj.get_counter(), safe=False)


class CloneComing(APIView):
  permission_classes = (IsAuthenticated, )
  def put(self, request, uuid, *args, **kwargs):
    coming = get_object_or_404(Coming, pk=uuid)
    status_coming_again = Status.objects.filter(name='Вторичка').first()
    coming.status_fk = status_coming_again
    coming.pk = None
    coming.save()
    serializer = ComingSerializer([coming], many=True)
    return Response(serializer.data[0], status=200)

  
class ThemeViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated, )
  queryset = Theme.objects.all().order_by('name')
  serializer_class = ThemeSerializer


class StatusViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated, )
  queryset = Status.objects.all().order_by('name')
  serializer_class = StatusSerializer
