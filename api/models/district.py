from django.db import models


class District(models.Timestamp):
    name = models.CharField(max_length=45)

    # Foreign keys
    province = models.ForeignKey(
        'Province',  # assumes you already have a Province model
        on_delete=models.CASCADE,
        related_name='districts'
    )
    
    def __str__(self):
        return self.name
