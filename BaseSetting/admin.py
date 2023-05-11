from django.contrib import admin
from BaseSetting.models import BaseSetting


@admin.register(BaseSetting)
class BaseSettingAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'value',
    'description',
    'app_fk',
  ]
