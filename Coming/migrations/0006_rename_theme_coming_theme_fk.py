# Generated by Django 4.1.7 on 2023-02-28 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coming', '0005_alter_theme_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coming',
            old_name='theme',
            new_name='theme_fk',
        ),
    ]
