from django.db import models
import uuid


class Department(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Наименование', max_length=300, unique=True)
  create_date = models.DateField('Дата создания', null=True, auto_now_add=True)

  class Meta():
    verbose_name = "Отдел"
    verbose_name_plural = "Отделы"

  def __str__(self):
    return self.name


class StatusPersone(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Статус', max_length=50)

  class Meta():
    verbose_name = "Статус сотрудника"
    verbose_name_plural = "Статусы сотрудников"

  def __str__(self):
    return self.name


class Personal(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=300)
  phone = models.CharField(max_length=12)
  department_fk = models.ForeignKey(Department, on_delete=models.CASCADE)
  pin = models.IntegerField(unique=True)
  status_fk = models.ForeignKey(StatusPersone, on_delete=models.PROTECT) 
  
  create_date = models.DateField('Дата создания', null=True, auto_now_add=True)

  class Meta():
    verbose_name = "Сотрудник"
    verbose_name_plural = "Сотрудники"

  def __str__(self):
    return self.name
