import django_filters as filters
from Agreement.models import Agreement


class AgreementFilter(filters.FilterSet):
  name = filters.CharFilter(lookup_expr='icontains', field_name='coming_fk__name')
  phone = filters.CharFilter(lookup_expr='icontains', field_name='coming_fk__client_fk__phone')
  number = filters.CharFilter(lookup_expr='icontains')
  note = filters.CharFilter(lookup_expr='icontains')
  theme_fk = filters.CharFilter(lookup_expr='exact', field_name='coming_fk__theme_fk__pk')
  service_fk = filters.CharFilter(lookup_expr='exact', field_name='service_fk__pk')

  class Meta:
    model = Agreement
    fields = {
      'number',
      'note',
    }
