from django.urls import path
from rest_framework.routers import DefaultRouter

from measurement.views import ListSensorsAPIView, ListMeasurementAPIView
urlpatterns = []

router = DefaultRouter()
router.register(r'sensors', ListSensorsAPIView)
router.register(r'measurements', ListMeasurementAPIView)
router.register(r'', ListMeasurementAPIView)
urlpatterns += router.urls

#print(urlpatterns)

urlpatterns += [
    # TODO: зарегистрируйте необходимые маршруты
    #path()
]

