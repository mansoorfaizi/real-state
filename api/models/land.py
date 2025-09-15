from django.db import models
from .timestamp import Timestamp
from .property import Property

class Land(Timestamp):
    area_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    land = models.CharField(max_length=45)
    document = models.CharField(max_length=45)
    road_access = models.CharField(max_length=200)
    nearby_facilities = models.CharField(max_length=45)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="lands")

    def __str__(self):
        return f"Land: {self.land}, Area: {self.area_m2} m²"