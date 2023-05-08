import django_filters as filters
from Cashbox.models import Cashbox


class CashboxFilter(filters.FilterSet):
  name = filters.CharFilter(lookup_expr='icontains')
  money = filters.CharFilter(lookup_expr='icontains')
  # call = filters.CharFilter(lookup_expr='iexact')
  # upp = filters.CharFilter(lookup_expr='iexact')
  # theme_fk__name = filters.CharFilter(lookup_expr='iexact')
  # status_fk_name = filters.CharFilter(lookup_expr='iexact')

  class Meta:
    model = Cashbox
    fields = {
      'name',
      # 'call',
      # 'upp',
      # 'theme_fk',
      # 'status_fk',
    }
