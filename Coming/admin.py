from django.contrib import admin
from Coming.models import (Coming, Theme, Status)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]


@admin.register(Coming)
class ComingAdmin(admin.ModelAdmin):
  search_fields = ['name']
  autocomplete_fields = ['client_fk', 'call_fk']
  filter_horizontal = ['upp']
  
  list_display = [
    'name',
    #'client_fk',
    'call_fk',
    #'upp',
    'theme_fk',
    'status_fk',
  ]

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]
