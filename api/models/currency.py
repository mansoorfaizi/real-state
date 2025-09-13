from .timestamp import Timestamp, models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Currency(Timestamp):
    name = models.CharField(max_length=45, unique=True) 
    symbol = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3)] 
    )

    def __str__(self):
        return f"{self.name} ({self.symbol})"
