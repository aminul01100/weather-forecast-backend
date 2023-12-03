from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# for GIS, usage of PointField is recommended. however, this is going to be a fast forwarded POC and use some fixtures,
# we will be using just a Decimal value field to store the coordinates
class District(models.Model):
    division_id = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bn_name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    long = models.DecimalField(max_digits=22, decimal_places=16)
    average_temperature = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.bn_name})"
