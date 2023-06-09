import django_filters as filters
from Coming.models import Coming


class ComingFilter(filters.FilterSet):
  name = filters.CharFilter(lookup_expr='icontains')
  phone = filters.CharFilter(lookup_expr='icontains', field_name='client_fk__phone')
  call_fk = filters.CharFilter(lookup_expr='iexact', field_name='call_fk__id')
  upp = filters.CharFilter(lookup_expr='iexact', field_name='upp__id')
  theme_fk__name = filters.CharFilter(lookup_expr='iexact')
  status_fk_name = filters.CharFilter(lookup_expr='iexact')
  create_date_time = filters.DateTimeFromToRangeFilter()

  class Meta:
    model = Coming
    fields = {
      'name',
      'call_fk',
      'upp',
      'theme_fk',
      'status_fk',
      'create_date_time',
    }
