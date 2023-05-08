from django.db import models
import uuid


class Client(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=300)
  phone = models.CharField(max_length=12, unique=True)
  create_date_time = models.DateTimeField('Дата создания', null=True, auto_now_add=True)

  class Meta():
    verbose_name = "Клиент"
    verbose_name_plural = "Клиенты"

  def __str__(self):
    return self.name
