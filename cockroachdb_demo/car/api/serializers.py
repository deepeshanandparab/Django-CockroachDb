from rest_framework.serializers import ModelSerializer
from car.models import Car

class CarCreateSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'car_brand', 'body_type', 'color', 'manufacturing_year']

class CarListSerialzer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'car_brand']

class CarDetailSerialzer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'car_brand', 'body_type', 'color', 'manufacturing_year']

class CarUpdateSerialzer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'car_brand', 'body_type', 'color', 'manufacturing_year']

class CarDeleteSerializer(ModelSerializer):
    class Meta:
        model: Car
        fields = ['name', 'car_brand', 'body_type', 'color', 'manufacturing_year']

