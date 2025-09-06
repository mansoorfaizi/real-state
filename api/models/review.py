from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from api.models.timestamp import Timestamp
from api.models.property import Property
from django.contrib.auth.models import User


class Review(Timestamp):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True
    )
    message = models.TextField()
    user = models.ForeignKey(User,  null=True, blank=True, related_name="reviews", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, null=True, blank=True, related_name="reviews", on_delete=models.CASCADE)
    
    def __str__(self):
        if self.rating:
            return f"Rating: {self.rating} Stars on {self.property.name if self.property else 'Unknown Property'}"
        return f"Review on {self.property.name if self.property else 'Unknown Property'}: {self.message[:50]}"
    
    class Meta:
        ordering = ['-created_at']
