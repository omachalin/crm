import django_filters as filters
from BaseSetting.models import BaseSetting


class BaseSettingFilter(filters.FilterSet):
  name = filters.CharFilter(lookup_expr='exact')
  app_fk = filters.CharFilter(lookup_expr='exact', field_name='app_fk__id')

  class Meta:
    model = BaseSetting
    fields = {
      'name',
      'app_fk',
    }
