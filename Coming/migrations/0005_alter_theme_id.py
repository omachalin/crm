# Generated by Django 4.1.7 on 2023-02-28 19:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Coming', '0004_alter_coming_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
