# Generated by Django 4.1.7 on 2023-05-09 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coming', '0014_coming_call'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coming',
            old_name='call',
            new_name='call_fk',
        ),
    ]
