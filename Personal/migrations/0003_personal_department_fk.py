# Generated by Django 4.1.7 on 2023-02-28 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='department_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Personal.department'),
            preserve_default=False,
        ),
    ]
