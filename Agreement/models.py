from django.db import models
import uuid
from Coming.models import Coming
from Cashbox.models import Cashbox


class Service(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Наименование', max_length=250)

  class Meta():
    verbose_name = "Сервис"
    verbose_name_plural = "Сервисы"

  def __str__(self):
    return self.name  


class Agreement(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  number = models.CharField(max_length=50)
  coming_fk = models.ForeignKey(Coming, on_delete=models.CASCADE)
  price = models.IntegerField(default=0)
  price_transport = models.IntegerField(default=0)
  service_fk = models.ForeignKey(Service, on_delete=models.PROTECT, blank=True, null=True)
  note = models.CharField(max_length=300, blank=True, null=True)
  dissolution = models.BooleanField(default=False)
  cashboxes = models.ManyToManyField(Cashbox, blank=True)
  create_date_time = models.DateTimeField('Дата создания', null=True, auto_now_add=True)

  class Meta():
    verbose_name = "Договор"
    verbose_name_plural = "Договоры"

  def __str__(self):
    return self.number

