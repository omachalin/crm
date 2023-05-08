from django.contrib import admin
from Client.models import (Client)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
  search_fields = ['name', 'phone']
  list_display = [
    'name',
    'phone',
  ]