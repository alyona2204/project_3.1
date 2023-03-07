import datetime

from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(verbose_name='Дата измерения', default=datetime.datetime.now, blank=True)
    image = models.ImageField(max_length=None, upload_to='meas')

    class Meta:
        verbose_name = 'Температура'
        verbose_name_plural = 'Температуры'
