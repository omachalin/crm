from django.db import models
from Client.models import (Client)
import uuid


class Theme(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=300)
  create_date = models.DateField('Дата создания', null=True, auto_now_add=True)


  class Meta():
    verbose_name = "Тематика"
    verbose_name_plural = "Тематики"

  def __str__(self):
    return self.name


class Status(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)

  class Meta():
    verbose_name = "Статус прихода"
    verbose_name_plural = "Статусы приходов"

  def __str__(self):
    return self.name


class Coming(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  client_fk = models.ForeignKey(Client, on_delete=models.CASCADE)
  name = models.CharField(max_length=300)
  #phone = models.CharField(max_length=12)
  call = models.IntegerField(null=True, blank=True)
  upp = models.IntegerField(null=True, blank=True)
  theme_fk = models.ForeignKey(Theme, on_delete=models.PROTECT, blank=True, null=True)
  status_fk = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
  create_date_time = models.DateTimeField('Дата создания', null=True, auto_now_add=True)

  class Meta():
    verbose_name = "Приход"
    verbose_name_plural = "Приходы"

  def __str__(self):
    return self.name
