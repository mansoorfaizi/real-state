from django.db import models

# Create your models here.
from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at} - {self.updated_at}"


class District(models.Model):
    name = models.CharField(max_length=45)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')
    timestamp = models.OneToOneField(Timestamp, on_delete=models.CASCADE, related_name='district')

    def __str__(self):
        return self.name
