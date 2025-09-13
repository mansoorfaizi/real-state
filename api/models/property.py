from django.db import models
from .timestamp import Timestamp
from .area import Area
from .currency import Currency

class Property(Timestamp):
    DEAL_TYPE_CHOICES = [
        ("sale", "Sale"),
        ("rent", "Rent"),
        ("mortgage", "Mortgage"),
    ]

    PROPERTY_TYPE_CHOICES = [
        ("house", "House"),
        ("apartment", "Apartment"),
        ("land", "Land"),
        ("office", "Office"),
    ]

    title = models.CharField(max_length=45)
    deal_type = models.CharField(max_length=45, choices=DEAL_TYPE_CHOICES)
    property_type = models.CharField(max_length=45, choices=PROPERTY_TYPE_CHOICES)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="properties")
    full_address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="properties")
    description = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.get_deal_type_display()} ({self.get_property_type_display()})"



class PropertyMedia(Timestamp):
    file = models.CharField(max_length=45)
    caption = models.CharField(max_length=45)

    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    property_area = models.ForeignKey("Area", on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.caption} ({self.file})"