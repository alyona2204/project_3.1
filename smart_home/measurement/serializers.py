from rest_framework import serializers
from django import forms

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    #sensor = SensorSerializer(read_only=True)
    image = serializers.ImageField(required=False)
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, m):
        return f'fff{m.image}{m.id}'
    class Meta:
        model = Measurement
        fields = ['id','sensor', 'temperature', 'created_at', 'image', 'image_url']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']



