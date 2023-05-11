from django.contrib import admin

from App.models import (App)


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    #'data',
  ]
