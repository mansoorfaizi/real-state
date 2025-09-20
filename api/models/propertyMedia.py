from django.db import models
from api.models.timestamp import Timestamp

class PropertyMedia(Timestamp):

    file = models.CharField(max_length=45)
    caption = models.CharField(max_length=45)

    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    property_area = models.ForeignKey("Area", on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.caption} ({self.file})"