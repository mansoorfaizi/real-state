from django.db import models
from django.core.validators import MinValueValidator
from api.models.timestamp import Timestamp
from api.models.property import Property


class Apartment(Timestamp):
    floor_number = models.IntegerField(validators=[MinValueValidator(0)])
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)])
    bathrooms = models.IntegerField(validators=[MinValueValidator(0),])
    area = models.IntegerField(validators=[MinValueValidator(1)])
    balcony = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    heating_system = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    building_management = models.BooleanField(default=False)

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="apartments"
    )

    def __str__(self):
        return f"Apartment (Floor {self.floor_number}, {self.bedrooms} BR, {self.area} m²)"
