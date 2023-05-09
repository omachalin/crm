import django_filters as filters
from Personal.models import Personal


class PersonalFilter(filters.FilterSet):
  name = filters.CharFilter(lookup_expr='icontains')
  pin = filters.CharFilter(lookup_expr='iexact')
  phone = filters.CharFilter(lookup_expr='icontains')
  status_fk = filters.CharFilter(lookup_expr='iexact', field_name='status_fk__id')

  class Meta:
    model = Personal
    fields = {
      'name',
      'phone',
      'pin',
      'status_fk',
    }
