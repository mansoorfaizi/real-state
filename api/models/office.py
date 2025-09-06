from django.db import models
from api.models.timestamp import Timestamp
from django.core.validators import MinValueValidator


class office(Timestamp):
    TOILET_CHOICES = [
        ("ATTACHED", "Attached"),
        ("SHARED", "Shared"),
    ]

    area = models.IntegerField()
    floor_number = models.IntegerField()
    number_of_rooms = models.IntegerField(validators=[MinValueValidator(1)])
    internet_access = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    security = models.BooleanField(default=True)
    toilet = models.CharField(max_length=10, choices=TOILET_CHOICES)

    property = models.ForeignKey(
        property,
        on_delete=models.CASCADE,
        related_name="office"
    )

    def __str__(self):
        return f"Office (Floor {self.floor_number}, {self.number_of_rooms} Rooms, {self.area} m²)"
