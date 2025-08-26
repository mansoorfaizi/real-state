from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Currency(models.Model):
    name = models.CharField(max_length=45, unique=True) 
    symbol = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3)] 
    )
    timestamp = models.ForeignKey(
        Timestamp, on_delete=models.CASCADE, related_name="currencies"
    )

    def __str__(self):
        return f"{self.name} ({self.symbol})"
