# Generated by Django 4.1.7 on 2023-02-28 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coming', '0007_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coming',
            name='status',
        ),
        migrations.AddField(
            model_name='coming',
            name='status_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Coming.status'),
        ),
    ]
