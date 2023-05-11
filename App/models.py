from django.db import models
import uuid


class App(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Наименование', max_length=300)
  #data = models.JSONField('Data', null=True, blank=True)

  class Meta():
    verbose_name = "Приложение"
    verbose_name_plural = "Приложения"

  def __str__(self):
    return self.name
