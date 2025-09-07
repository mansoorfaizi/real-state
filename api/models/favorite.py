from django.db import models
from api.models.timestamp import Timestamp
from api.models.property import Property
from django.contrib.auth.models import User
class Favorite(Timestamp):
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name="favorites", on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'property')   # A user cannot favorite the same property twice
        ordering = ['-created_at'] 
    def __str__(self):
        return f"{self.user.username} -> {self.property.title}"
