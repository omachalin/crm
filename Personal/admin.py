from django.contrib import admin
from Personal.models import (Personal, Department, StatusPersone)


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
  search_fields = ['name', 'phone']
  list_display = [
    'name',
    'phone',
    'department_fk',
    'pin',
    'status_fk',
  ]


@admin.register(StatusPersone)
class StatusPersoneAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
  list_display = [
    'name',
  ]
