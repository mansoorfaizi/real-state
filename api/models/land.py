from django.db import models
from api.models.timestamp import Timestamp
from api.models.property import Property
from django.core.validators import MinValueValidator

class Land(Timestamp):
    LAND_TYPE = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Agricultural', 'Agricultural'),
    ]
    DOCS_TYPE = [
        ('Official', 'Official'),
        ('Customary', 'Customary'),
    ]
    ROAD_ACCESS = [
        ('Paved', 'Paved'),
        ('Unpaved', 'Unpaved'),
    ]

    area_m2 = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    land_type = models.CharField(max_length=20, choices=LAND_TYPE)
    docs_type = models.CharField(max_length=20, choices=DOCS_TYPE)
    road_access = models.CharField(max_length=20, choices=ROAD_ACCESS)
    nearby_facilities = models.TextField(blank=True)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True, related_name="lands")

    def __str__(self):
        return f"Land {self.property.id if self.property else 'N/A'} - {self.land_type}"
