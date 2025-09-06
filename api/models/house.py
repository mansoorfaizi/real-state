from django.db import models
from django.core.validators import MinValueValidator
from api.models.timestamp import Timestamp
from api.models.property import Property

class House(Timestamp):
    WATER_CHOICES = [
        ('City', 'City'),
        ('Well', 'Well'),
        ('Tank', 'Tank'),
    ]
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)])                   
    bathrooms = models.IntegerField(validators=[MinValueValidator(0)])                  
    total_area_m2 = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])   
    built_area_m2 = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  
    floors_no = models.IntegerField(validators=[MinValueValidator(0)])   
    water_type = models.CharField(max_length=10, choices=WATER_CHOICES)                  
    parking = models.BooleanField(default=False)      
    heating_system = models.BooleanField(default=True)   
    electricity = models.BooleanField(default=True)   
    official_docs = models.BooleanField(default=True)   
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True, related_name="houses")

    def __str__(self):
        return f"House {self.property.id if self.property else 'N/A'} - {self.bedrooms} BR, {self.bathrooms} Bath"
