from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=20)
    body_type = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    manufacturing_year = models.IntegerField(default=0)



