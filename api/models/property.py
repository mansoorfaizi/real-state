from django.db import models
from .timestamp import Timestamp
from .area import Area
from .currency import Currency

class Property(Timestamp):
    title = models.CharField(max_length=45)
    detail_type = models.CharField(max_length=45)
    property_type = models.CharField(max_length=45)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    full_address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    description = models.TextField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()

    def __str__(self):
        return self.title
