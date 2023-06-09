# Generated by Django 4.1.7 on 2023-03-01 12:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('data', models.JSONField(blank=True, null=True, verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
    ]
