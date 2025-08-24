from django.db import models

# Create your models here.
class Timestamp(models.Model):
    created_at = models.CharField(max_length=45)
    updated_at = models.CharField(max_length=45)