from django.contrib import admin
from Agreement.models import Agreement, Service


class CashboxInline(admin.TabularInline):
  model = Agreement.cashboxes.through
  autocomplete_fields = ['cashbox']
  readonly_fields = ['get_money']

  def get_money(self, instance):
    return instance.cashbox.money
  get_money.short_description = 'Money'


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
  search_fields = ['number', 'cashboxes__name', 'coming_fk__name']
  inlines = [CashboxInline]
  exclude = ('cashboxes',)
  list_display = [
    'number',
    'coming_fk',
    'price',
    'price_transport',
    'dissolution',
    'note',
  ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]