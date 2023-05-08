from django.db import models
import uuid
from django.core.validators import MinValueValidator
from django.contrib import admin


class TypePayment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Наименование', max_length=50)

  class Meta():
    verbose_name = "Тип платежа"
    verbose_name_plural = "Типы платежей"

  def __str__(self):
    return self.name


class Cashbox(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Наименование', max_length=255)
  money = models.IntegerField('Деньги', validators=[
    MinValueValidator(1)
  ])
  type_payment_fk = models.ForeignKey(TypePayment, on_delete=models.PROTECT)
  create_date_time = models.DateTimeField('Дата создания', null=True, auto_now_add=True)

  class Meta():
    verbose_name = "Касса"
    verbose_name_plural = "Касса"

  def __str__(self):
    return str(self.name)

  class CashboxAdmin(admin.ModelAdmin):
    search_fields = ['name', 'money']  # добавляем поле 'money' в поиск

