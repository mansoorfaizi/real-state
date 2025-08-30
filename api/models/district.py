from django.db import models

class District(models.Model):
    name = models.CharField(max_length=45)

    # Foreign keys
    province = models.ForeignKey(
        'Province',  # assumes you already have a Province model
        on_delete=models.CASCADE,
        related_name='districts'
    )
    timestamp = models.OneToOneField(
        'Timestamp',  # assumes you already have a Timestamp model
        on_delete=models.CASCADE,
        related_name='district'
    )

    def __str__(self):
        return self.name
