from django.db import models


class Timestamp(models.Model):
    created_at = models.CharField(max_length=45)
    updated_at = models.CharField(max_length=45)

    class Meta:
        abstract = True