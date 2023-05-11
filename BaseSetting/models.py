from django.db import models
from App.models import App
import uuid


class BaseSetting(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Ключ', max_length=120)
  value = models.CharField('Значение', max_length=250)
  description = models.CharField('Описание', max_length=500)
  app_fk = models.ForeignKey(App, on_delete=models.CASCADE, verbose_name='Приложение')

  class Meta():
    verbose_name = "Базовая настройка"
    verbose_name_plural = "Базовые настройки"

  def __str__(self):
    return self.name
