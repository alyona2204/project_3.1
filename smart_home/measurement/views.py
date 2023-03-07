# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.viewsets import ModelViewSet


class ListSensorsAPIView(ModelViewSet):
    #serializer_class = SensorDetailSerializer
    def get_serializer_class(self):
        print(self.action)
        if 'list' == self.action:
            return SensorSerializer
        return SensorDetailSerializer
    queryset = Sensor.objects.all()

    search_fields = ["id"]
    filterset_fields = search_fields


class ListMeasurementAPIView(ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

    search_fields = ["id"]
    filterset_fields = search_fields
