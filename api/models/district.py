from .timestamp import Timestamp, models

class District(Timestamp):
    name = models.CharField(max_length=45)
    province = models.ForeignKey(
        'Province',
        on_delete=models.CASCADE,
        related_name='districts'
    )
    
    def __str__(self):
        return self.name
