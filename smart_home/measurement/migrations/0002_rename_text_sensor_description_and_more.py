# Generated by Django 4.1.4 on 2023-03-01 18:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='text',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='date_of_measurement',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='id_sensor',
        ),
        migrations.AddField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата измерения'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
            preserve_default=False,
        ),
    ]