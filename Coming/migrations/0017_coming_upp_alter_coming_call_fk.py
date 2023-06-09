# Generated by Django 4.1.7 on 2023-05-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0005_personal_status_fk'),
        ('Coming', '0016_remove_coming_upp'),
    ]

    operations = [
        migrations.AddField(
            model_name='coming',
            name='upp',
            field=models.ManyToManyField(to='Personal.personal', verbose_name='ЮПП'),
        ),
        migrations.AlterField(
            model_name='coming',
            name='call_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='calls', to='Personal.personal', verbose_name='Оператор'),
        ),
    ]
