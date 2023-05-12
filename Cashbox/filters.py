import django_filters as filters
from Cashbox.models import Cashbox, TypePayment


class CashboxFilter(filters.FilterSet):
  name = filters.CharFilter(lookup_expr='icontains')
  money = filters.CharFilter(lookup_expr='icontains')
  type_payment_fk = filters.ModelMultipleChoiceFilter(
    field_name='type_payment_fk',
    to_field_name='id',
    queryset=TypePayment.objects.all(),
  )
  create_date_time = filters.DateTimeFromToRangeFilter()

  class Meta:
    model = Cashbox
    fields = {
      'name',
      'money',
      'type_payment_fk',
      'create_date_time',
    }
    ordering = ('create_date_time',)
