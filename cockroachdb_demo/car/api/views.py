from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from car.models import Car
from car.api.serializers import (
    CarCreateSerializer,
    CarListSerialzer,
    CarDetailSerialzer,
    CarUpdateSerialzer,
    CarDeleteSerializer
)

class CarCreateApiView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

class CarListApiView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerialzer

class CarDetailApiView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerialzer

class CarUpdateApiView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerialzer

class CarDeleteApiView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDeleteSerializer

