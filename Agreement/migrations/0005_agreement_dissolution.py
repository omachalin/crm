# Generated by Django 4.1.7 on 2023-03-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agreement', '0004_agreement_create_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='dissolution',
            field=models.BooleanField(default=False),
        ),
    ]
