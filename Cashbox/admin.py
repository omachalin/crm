from django.contrib import admin
from Cashbox.models import TypePayment, Cashbox, TypeMoney


@admin.register(TypePayment)
class TypePaymentAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]


@admin.register(TypeMoney)
class TypeMoneyAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]


@admin.register(Cashbox)
class CashboxAdmin(admin.ModelAdmin):
  search_fields = ['name']
  list_display = [
    'name',
    'money',
    'type_payment_fk',
  ]
